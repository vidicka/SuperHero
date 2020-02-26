"""
Imports superhero stats and saves them localy for further use, available offline
"""

import json
import requests
import re
import pickle
from random import randint


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
		self.health = int(durability)*3

	@property
	def id_nr(self):
		return self.__id_nr

	@id_nr.setter
	def id_nr(self, id_nr):
		self.__id_nr = id_nr


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

	def random_hero(hero_list):

		hero_cnt = len(hero_list)
		
		while True:
			rand = randint(1,hero_cnt)

			hero = hero_list[rand-1]

			if hero.publisher == "DC Comics" or hero.publisher == "Marvel Comics":
				return hero

	def hero_to_fight(self):
		return Hero_fight(self.id_nr, self.name, self.intelligence, self.strength, self.speed, self.durability, self.power, self.combat, self.image, self.publisher, self.img_url)



class Hero_fight(Hero):

	def __init__(self, id_nr, name, intelligence, 
		strength, speed, durability, power, combat, image, publisher, img_url, power_up=0, round_cnt=0):
		Hero.__init__(self, id_nr, name, intelligence, strength, speed, durability, power, combat, image, publisher, img_url)

		self.health = int(self.durability)*3 + 100
		self.power_up = power_up
		self.round_cnt = round_cnt



	def attack(self, attack_type):
		if attack_type == 'melee':
			dice_cnt = (int(self.strength) + int(self.combat))//10
		elif attack_type == 'ranged':
			dice_cnt = (int(self.speed) + int(self.combat))//10
		pwr = self.power_up
		self.power_up = 0

		return Hero_fight.throw_dice(dice_cnt) + pwr		

	
	def power_up_hero(self):
		
		if self.intelligence > self.power:
			dice_cnt = (int(self.intelligence) + int(self.combat))//10
		else:
			dice_cnt = (int(self.power) + int(self.combat))//10

		self.power_up = Hero_fight.throw_dice(dice_cnt)



	def throw_dice(dice_cnt):
		dmg = 0
		for _ in range(dice_cnt):
			dmg += randint(1,10)
		return dmg

	def take_dmg(self, dmg):
		if self.health - dmg <= 0:
			self.health = 0
		else:
			self.health -= dmg/2  

	def choose_attack(self):
		attacks = ['melee','ranged','power_up']

		if (self.round_cnt ) % 3 == 0:
			ind = randint(0,2)
		else:
			ind = randint(0,1)

		print(attacks[ind])
		return(attacks[ind])


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
		hero =(Hero(i+1, name, intelligence,strength, speed, durability, power, combat, image, publisher, img_url))

		if hero.publisher == "DC Comics" or hero.publisher == "Marvel Comics":
			all_heroes.append(hero)

	with open('heroes.pickle', 'wb') as heroes:
		pickle.dump(all_heroes, heroes)


if __name__ == "__main__":
	main()
