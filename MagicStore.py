import MagicCardInstance


class MagicStore:
    instances = list()

    def __init__(self, name: str):
        self.instances.append(self)
        self.name = name
        self.cards = list()

    def add_card(self, card: MagicCardInstance):
        self.cards.append(card)

    @staticmethod
    def get_all_stores():
        return MagicStore.instances
