import MagicCard
import MagicStore


class MagicCardInstance:
    instances = list()

    def __init__(self, price: float, quality: str, quantity: int, language: str, edition: str, foil: bool, card: MagicCard, store: MagicStore):
        self.instances.append(self)
        self.price = price
        self.quality = quality
        self.quantity = quantity
        self.language = language
        self.edition = edition
        self.foil = foil
        self.card = card
        self.store = store

    def __str__(self):
        return str(self.card) + ';' + str(self.store) + ';' + str(self.price) + ';' + self.quality + ';' + str(self.quantity) + ';' + self.language + ';' + self.edition + ';' + str(self.foil)
