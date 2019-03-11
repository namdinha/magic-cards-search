from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from MagicCardInstance import MagicCardInstance
from MagicStore import MagicStore
from MagicCard import MagicCard
from selenium.webdriver.chrome.options import Options
import re


class CardSearch:
	def __init__(self):
		options = Options()
		options.headless = True
		self.driver = webdriver.Chrome('D:\Documentos\selenium\chromedriver', chrome_options=options)
		# self.driver = webdriver.Chrome()

	def enter_site(self):
		self.driver.get("https://www.ligamagic.com.br")
		# self.driver.find_element_by_id("campanha-del-1").click()

	def search_card(self, card: MagicCard, links: dict):
		for store, link in links.items():
			self.driver.get(link)
			html_instances = self.driver.find_elements_by_xpath("//div[@class='itemMain']/table/tbody/tr/td[2]/div[2]/table/tbody/tr")
			html_instances = html_instances[1:]
			for html_instance in html_instances:
				html_instance_attributes = html_instance.find_elements_by_xpath(".//td")
				print(card.name + store.name + html_instance.text)
				matching = re.search(r'  (.*?) (.*) (.*?) unid. (.*)', html_instance.text)
				quantity = int(matching.group(3))
				if quantity == 0:
					break
				edition = html_instance_attributes[0].find_element_by_xpath(".//a/img").get_attribute("title")
				language = matching.group(1)
				quality = matching.group(2)
				price = float(matching.group(4).split()[1].replace(".", "").replace(",", "."))
				foil = False
				card_instance = MagicCardInstance(price, quality, quantity, language, edition, foil, card)
				card.add_instance(card_instance)

	def search_cards(self, card_names: list, store_names: list):
		cards = list()
		for card_name in card_names:
			card = MagicCard(card_name)
			name_to_search = card_name.replace(" ", "+")
			self.driver.get("https://www.ligamagic.com.br/?view=cards/card&card=" + name_to_search)
			if "Busca de Cards" in self.driver.title:
				store_links = dict(map(lambda x: (MagicStore(x.find_element_by_xpath(".//img").get_attribute("title")), x.get_attribute("href")) if x.find_element_by_xpath(".//img").get_attribute("title") in store_names else (None, None), self.driver.find_elements_by_xpath("//div[@class='e-col1']/a")))
				store_links.pop(None, None)
			else:
				continue
			self.search_card(card, store_links)
			cards.append(card)
		return cards

	def search(self, card_name):
		search = self.driver.find_element_by_id("query")
		search.clear()
		search.send_keys(card_name)
		search.send_keys(Keys.RETURN)

	@staticmethod
	def save(cards: list):
		file = open("cards.txt", "a+")
		for card in cards:
			for store in MagicStore.get_all_stores():
				for card_instance in card.get_instances_in_store(store):
					continue
		file.close()
