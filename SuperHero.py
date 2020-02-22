"""
Imports superhero stats and saves them localy for further use, available offline
"""

import json
import requests
import re
import pickle


class Hero:

	def __init__(self, id_nr, name, intelligence, 
		strength, speed, durability, power, combat, image, publisher, img_url):
		"""
		Creates an instance of Hero class
		"""
		self.__id_nr = id_nr
		self.__name = name
		self.__intelligence = intelligence
		self.__strength = strength
		self.__speed = speed
		self.__durability = durability
		self.__power = power
		self.__combat = combat
		self.__image = image
		self.__publisher = publisher
		self.img_url = img_url

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, name):
		self.__name = name


	@property
	def intelligence(self):
		return self.__intelligence

	@intelligence.setter
	def intelligence(self, intelligence):
		self.intelligence = intelligence


	@property
	def strength(self):
		return self.__strength

	@strength.setter
	def strength(self, strength):
		self.__strength = strength


	@property
	def speed(self):
		return self.__speed

	@speed.setter
	def speed(self, speed):
		self.__speed = speed


	@property
	def durability(self):
		return self.__durability

	@durability.setter
	def durability(self, durability):
		self.__durability = durability


	@property
	def power(self):
		return self.__power

	@power.setter
	def power(self, power):
		self.__power = power


	@property
	def combat(self):
		return self.__combat

	@combat.setter
	def combat(self, combat):
		self.__combat = combat


	@property
	def image(self):
		return self.__image

	@image.setter
	def image(self, image):
		self.__image = image


	@property
	def publisher(self):
		return self.__publisher

	@publisher.setter
	def publisher(self, publisher):
		self.__publisher = publisher


	def __str__(self):
		return f"{self.__id_nr}. {self.__name} \nINT: {self.__intelligence} \nSTR: {self.__strength} \nSPD: {self.__speed} \nDUR: {self.__durability} \nPOW: {self.__power} \nCMB: {self.__combat} \nPUBLISHER: {self.__publisher}"

	def __repr__(self):
		return f"Hero({self.__id_nr}, {self.__name}, {self.__intelligence}, {self.__strength}, {self.__speed}, {self.__durability}, {self.__power}, {self.__combat}, {self.__image}, {self.__publisher})"

	def hero_stats(self):
		"""
		Returns hero stats in one row	
		"""
		return f"{self.__id_nr}. {self.__name} - INT: {self.__intelligence} STR: {self.__strength} SPD: {self.__speed} DUR: {self.__durability} POW: {self.__power} CMB: {self.__combat}"



def main():

	all_heroes=[]

	#URL for the whole list of superheroes and their stats
	all_stats = requests.get("https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/all.json")

	powerstats = requests.get("https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/powerstats/70.json")
	connections = requests.get("https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/connections/1.json")
	hero_id = requests.get("https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/id/1.json")


	hero_count = all_stats.text.count('"id":')

	for i in range (hero_count):

		#URL for power stats for each hero
		power_url = f"https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/powerstats/{i+1}.json" 
		#URL for other information about a hero
		id_url = f"https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/id/{i+1}.json"		


		powerstats = requests.get(power_url)
		hero_id = requests.get(id_url)

		compiled_re_id = re.compile('name": "(.*)"(.|\n)*"publisher": "(.*)"(.|\n)*"sm": "(.*)"')
		for match_id in compiled_re_id.finditer(hero_id.text):
			name = match_id.group(1)
			publisher = match_id.group(3)
			img_url = match_id.group(5)

		responce = requests.get(img_url)
		image = responce.content

		compiled_re_pow = re.compile('"intelligence": (\d*)(.|\n)*"strength": (\d*)(.|\n)*"speed": (\d*)(.|\n)*"durability": (\d*)(.|\n)*"power": (\d*)(.|\n)*"combat": (\d*)')
		for match_stat in compiled_re_pow.finditer(powerstats.text):
			intelligence = match_stat.group(1)
			strength = match_stat.group(3)
			speed = match_stat.group(5)		
			durability = match_stat.group(7)
			power = match_stat.group(9)
			combat = match_stat.group(11)

		all_heroes.append(Hero(i+1, name, intelligence,strength, speed, durability, power, combat, image, publisher, img_url))

	with open('heros.pickle', 'wb') as heroes:
		pickle.dump(all_heroes, heroes)


if __name__ == "__main__":
	main()
