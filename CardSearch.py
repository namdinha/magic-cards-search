from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

from MagicCardInstance import MagicCardInstance
from MagicStore import MagicStore
from MagicCard import MagicCard
from selenium.webdriver.chrome.options import Options
import re


class CardSearch:
	qualities = ["NM", "M", "SP", "MP", "HP", "D"]

	def __init__(self):
		options = Options()
		options.headless = True
		self.driver = webdriver.Chrome(chrome_options=options)
		# self.driver = webdriver.Chrome()

	def search_card(self, card: MagicCard, links: dict):
		for store, link in links.items():
			self.driver.get(link)
			html_instances = self.driver.find_elements_by_xpath("//div[@class='itemMain']/table/tbody/tr/td[2]/div[2]/table/tbody/tr")
			html_instances = html_instances[1:]
			for html_instance in html_instances:
				card_instance = self.make_card_instance(html_instance, card, store)
				card.add_instance(card_instance)
				store.add_card(card_instance)

	def search_cards(self, card_names: list, store_names: list):
		cards = list()
		for card_name in card_names:
			card = MagicCard(card_name)
			name_to_search = card_name.replace(" ", "+")
			self.driver.get("https://www.ligamagic.com.br/?view=cards/card&card=" + name_to_search)
			if "Busca de Cards" in self.driver.title:
				store_links = dict(map(
					lambda a:
					(MagicStore(a.find_element_by_xpath(".//img").get_attribute("title")), a.get_attribute("href"))
					if a.find_element_by_xpath(".//img").get_attribute("title") in store_names
					else (None, None),
					self.driver.find_elements_by_xpath("//div[@class='e-col1']/a")))
				store_links.pop(None, None)
			else:
				print("Could not find the card: " + card_name)
				continue
			self.search_card(card, store_links)
			cards.append(card)
		return cards

	def make_card_instance(self, html_element: WebElement, card: MagicCard, store: MagicStore):
		html_instance_attributes = html_element.find_elements_by_xpath(".//td")
		matching = re.search(r'  (.*?) (.*) (.*?) unid. (.*) (.*$)', html_element.text, re.S)
		quantity = int(matching.group(3))
		if quantity == 0:
			return None
		edition = html_instance_attributes[0].find_element_by_xpath(".//a/img").get_attribute("title")
		language = matching.group(1)
		quality = next(filter(lambda x: x in matching.group(2), self.qualities))
		price = float(matching.group(5).replace(".", "").replace(",", "."))
		foil = True if "Foil" in matching.group(2) else False
		return MagicCardInstance(price, quality, quantity, language, edition, foil, card, store)
