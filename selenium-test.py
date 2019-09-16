import MagicCard
from CardSearch import CardSearch
from IO import IO


def main():
	search = CardSearch()
	r = search.search_cards(["Tatyova, Benthic Druid",
"Budoka Gardener",
"Burnished Hart",
"Coiling Oracle",
"Dawntreader Elk",
"Diligent Farmhand",
"Dreamscape Artist",
"Dryad Greenseeker",
"Elvish Rejuvenator",
"Farhaven Elf",
"Fertilid",
"Floodbringer",
"Kefnet the Mindful",
"Llanowar Scout",
"Meloku the Clouded Mirror",
"Oboro Breezecaller",
"Psychosis Crawler",
"Rampaging Baloths",
"Roil Elemental",
"Sakura-Tribe Elder",
"Sakura-Tribe Scout",
"Skyshroud Ranger",
"Soratami Cloudskater",
"Sporemound",
"Walking Atlas",
"Wood Elves",
"World Shaper",
"Yavimaya Granger",
"Abundance",
"Animist's Awakening",
"Broken Bond",
"Crawling Sensation",
"Cultivate",
"Elixir of Immortality",
"Enter the Unknown",
"Excavation",
"Explore",
"Explosive Vegetation",
"Gaea's Touch",
"Ghirapur Orrery",
"Harrow",
"Horn of Greed",
"Journey of Discovery",
"Khalni Gem",
"Khalni Heart Expedition",
"Mana Breach",
"Path of Discovery",
"Rampant Growth",
"Retreat to Coralhelm",
"Rites of Flourishing",
"Seed the Land",
"Splendid Reclamation",
"Storm Cauldron",
"Summer Bloom",
"The Mending of Dominaria",
"Trade Routes",
"Zendikar's Roil",
"Bant Panorama",
"Blighted Woodland",
"Coral Atoll",
"Evolving Wilds",
"Myriad Landscape",
"Simic Growth Chamber",
"Terminal Moraine",
"Terramorphic Expanse",
"Warped Landscape"], ["Nerdz Cards", "Pharaoh\\\'s Shop", "Magicbembarato", "Bazar de Bagdá", "Magic House Games"])

	IO.save(r, "tatyova")
	print("debug")


if __name__ == "__main__":
	main()
