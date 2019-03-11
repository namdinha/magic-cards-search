from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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

			instances = self.driver.find_elements_by_xpath("//div[@class='itemMain']/table/tbody/tr/td[2]/div[2]/table/tbody/tr")
			instances = instances[1:]
			for instance in instances:
				inst = instance.find_elements_by_xpath(".//td")
				print(card.name + store + instance.text)
				matching = re.search(r'  (.*?) (.*) (.*?) unid. (.*)', instance.text)

				quantity = int(matching.group(3))
				if quantity == 0:
					break
				edition = inst[0].find_element_by_xpath(".//a/img").get_attribute("title")
				language = matching.group(1)
				quality = matching.group(2)
				price = float(matching.group(4).split()[1].replace(".", "").replace(",", "."))

				card.add_instance(store, price, quality, quantity, language, edition)

	def search_cards(self, card_names: list, stores: list):
		cards = list()
		for card_name in card_names:
			self.enter_site()
			card = MagicCard(card_name)
			link_name = card_name.replace(" ", "+")
			self.driver.get("https://www.ligamagic.com.br/?view=cards/card&card=" + link_name)
			store_links = []
			if ("Busca de Cards" in self.driver.title):
				store_links = dict(map(lambda x: (x.find_element_by_xpath(".//img").get_attribute("title"), x.get_attribute("href")) if x.find_element_by_xpath(".//img").get_attribute("title") in stores else (None, None), self.driver.find_elements_by_xpath("//div[@class='e-col1']/a")))
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

	def is_required_store(self, stores):
		if any(x in self.driver.title for x in stores):
			return True
		else:
			return False

	def save(self, cards: list):
		file = open("cards.txt", "a+")

		for card in cards:
			for store, instances in card.instances.items():
				for instance in instances:
					file.write(
						card.name + "," + store + "," + instance.edition + "," + instance.language + "," + instance.quality + "," + str(
							instance.quantity) + "," + str(instance.price) + "\n")

		file.close()

	def filter_cards(self, cards: list):

		def getKey(item):
			return item.price

		sum(lambda card: min(card.instances.values(), key=getKey), cards)

		for store, instances in card.instances.items():
			min = instances[0]
			for instance in instances:
				if "SP" in instance.quality or "NM" in instance.quality:
