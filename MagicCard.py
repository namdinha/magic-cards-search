import MagicCardInstance
from MagicStore import MagicStore


class MagicCard:
    all_cards = list()

    def __init__(self, name: str):
        self.all_cards.append(self)
        self.name = name
        self.instances = list()

    def add_instance(self, instance: MagicCardInstance):
        if instance is not None:
            self.instances.append(instance)

    def calculate_min_price(self):
        def get_key(item):
            return item.price
        return min(self.instances, key=get_key)

    @staticmethod
    def calculate_min_price_of_cards(cards: list):
        result = dict()
        for card in cards:
            result[card] = card.calculate_min_price()
        return result

    @staticmethod
    def calculate_min_price_of_deck(cards: list):
        return sum(card.price for card in MagicCard.calculate_min_price_of_cards(cards).values())

    def get_instances_in_store(self, store: MagicStore):
        return filter(lambda x: True if store is x.store else False, self.instances)

    def __str__(self):
        return self.name
