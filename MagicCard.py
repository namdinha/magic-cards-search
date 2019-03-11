from itertools import chain


class MagicCard:
    class MagicCardInstance:
        def __init__(self, price: float, quality: str, quantity: int, language: str, edition: str):
            self.price = price
            self.quality = quality
            self.quantity = quantity
            self.language = language
            self.edition = edition

    def __init__(self, name: str):
        self.name = name
        self.instances = dict()

    def add_instance(self, store: str, price: float, quality: str, quantity: int, language: str, edition: str):
        if store in self.instances:
            self.instances.get(store).append(self.MagicCardInstance(price, quality, quantity, language, edition))
        else:
            self.instances[store] = [self.MagicCardInstance(price, quality, quantity, language, edition)]

    def calculate_min(self):
        def get_key(item):
            return item.price

        return min(list(chain.from_iterable(self.instances.values())), key=get_key)

    @staticmethod
    def calculate_mins(cards: list):

        for card in cards:


