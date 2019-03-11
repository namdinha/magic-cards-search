import MagicCardInstance


class MagicCard:
    def __init__(self, name: str):
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

