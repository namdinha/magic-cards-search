import MagicCard
from CardSearch import CardSearch

def main():
	search = CardSearch()
	r = search.search_cards(["Angel of Glory's Rise",
	                         "Blood Artist",
	                         "Edgewalker ",
	                         "Harvester of Souls ",
	                         "Indulgent Tormentor ",
	                         "Ob Nixilis, Unshackled",
	                         "Razaketh, the Foulblooded",
	                         "Recruiter of the Guard",
	                         "Rune-Scarred Demon",
	                         "Shadowborn Apostle",
	                         "Xathrid Necromancer",
	                         "Zulaport Cutthroat",
	                         "Black Market",
	                         "Dictate of Erebos",
	                         "Grave Pact",
	                         "Phyrexian Arena",
	                         "Remembrance",
	                         "Cabal Coffers",
	                         "Godless Shrine",
	                         "Homeward Path",
	                         "Orzhov Basilica",
	                         "Reliquary Tower",
	                         "Scoured Barrens",
	                         "Strip Mine",
	                         "Urborg, Tomb of Yawgmoth",
	                         "Bontu's Monument",
	                         "Expedition Map",
	                         "Gilded Lotus",
	                         "Mind's Eye",
	                         "Phyrexian Altar",
	                         "Skullclamp",
	                         "Sol Ring",
	                         "Thrumming Stone",
	                         "Demonic Tutor",
	                         "Idyllic Tutor",
	                         "Immortal Servitude",
	                         "Merciless Eviction",
	                         "Secret Salvage",
	                         "Steelshaper's Gift",
	                         "Tendrils of Agony",
	                         "Unburial Rites",
	                         "Anguished Unmaking",
	                         "Enlightened Tutor",
	                         "Faith's Reward",
	                         "Utter End"], ["Nerdz Cards", "Pharaoh\\\'s Shop", "Magicbembarato", "Bazar de Bagdá"])

	CardSearch.save(r)
	print("debug")


if __name__ == "__main__":
	main()
