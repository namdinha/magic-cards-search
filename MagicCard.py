import MagicCardInstance
from MagicStore import MagicStore


class MagicCard:
    instances = list()

    def __init__(self, name: str):
        self.instances.append(self)
        self.name = name
        self.instances = list()

    def add_instance(self, instance: MagicCardInstance):
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

    def get_instances_in_store(self, store: MagicStore):
        return filter(lambda x: True if store in x.stores else False, self.instances)
