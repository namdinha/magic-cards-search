from MagicCard import MagicCard
from MagicStore import MagicStore


class IO:
    @staticmethod
    def save(cards: list, deck_name: str):
        file = open(deck_name + ".txt", "a+")
        for card in cards:
            for store in MagicStore.get_all_stores():
                for card_instance in card.get_instances_in_store(store):
                    file.write(str(card_instance) + "\n")
        file.write(str(MagicCard.calculate_min_price_of_deck(cards)))
        file.close()
