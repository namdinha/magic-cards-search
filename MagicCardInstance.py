import MagicCard
import MagicStore


class MagicCardInstance:
    instances = list()

    def __init__(self, price: float, quality: str, quantity: int, language: str, edition: str, foil: bool, card: MagicCard):
        self.instances.append(self)
        self.price = price
        self.quality = quality
        self.quantity = quantity
        self.language = language
        self.edition = edition
        self.foil = foil
        self.card = card
        self.stores = list()

    def add_store(self, store: MagicStore):
        self.stores.append(store)
