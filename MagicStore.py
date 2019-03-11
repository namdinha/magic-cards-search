import MagicCardInstance


class MagicStore:
    def __init__(self, name: str):
        self.name = name
        self.cards = list()

    def add_card(self, card: MagicCardInstance):
        self.cards.append(card)
