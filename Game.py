
from SuperHero import Hero
import pickle
import os
import requests

if __name__ == "__main__":
	with open('heroes.pickle', 'rb') as heroes:
		all_heroes = pickle.load(heroes)

	# hero1 = Hero.random_hero(all_heroes)
	# print(hero1)

	# with open('heroes.pickle', 'rb') as heroes:
 # 		all_heroes = pickle.load(heroes)

	# print (all_heroes[2])

	print(all_heroes[534])
    # command = 'python SuperHero.py'
    # os.system(command)

	# with open('heroji1.csv', 'w') as heroji:
	# 	heroji.write(f"jesam")


# with open('heroji.csv', 'w') as heroji:
# 	for hero in all_heroes:
# 		heroji.write(f"{hero.hero_csv()}\n")

# for hero in all_heroes: 
# 	print(hero.hero_csv())

# with open('image_c.jpg', 'wb') as img:
# 	img.write(all_heroes[70].image)


# with open('image_h.jpg', 'wb') as img:
# 	img.write(all_heroes[69].image)

