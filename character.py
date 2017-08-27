from data_and_enums import *
import random

class Character:
	def __init__(self, char_race, char_class, subrace):
		self.char_race 	= char_race
		self.char_class = char_class
		self.subrace 	= subrace

		self.class_data = class_data_dict[char_class]
		self.race_data = race_data_dict[char_race]
		if subrace:
			self.subrace_data = subrace_data_dict[subrace]
		else:
			self.subrace_data = None

		self.str = 0
		self.dex = 0
		self.con = 0
		self.int = 0
		self.wis = 0
		self.cha = 0
		self.hit_die = class_data_dict[char_class]["hit_die"]

		#Have to make a copy otherwise modifying languages modifies the languages
		#in race_data_dict - I should learn/use functional programming
		self.languages = {l for l in self.race_data["languages"]}
		
		if self.race_data["extra_language"]:
			language_choice = random.sample([l for l in language_list if l not in self.languages], 1)[0]
			self.languages.add(language_choice)

		self.skills = []

	def setAbilityScores(self, strength, dexterity, constitution, intelligence, wisdom, charisma):
		self.str = strength
		self.dex = dexterity
		self.con = constitution
		self.int = intelligence
		self.wis = wisdom
		self.cha = charisma

	# Takes list of ints in order of
	# str, dex, con, int, wis, cha
	# and a dict of {Abilities : int} and applies
	# the increases to the appropriate ability
	def applyAbilityIncreases(self, increases):
		for ability in increases:
			amount = increases[ability]
			if ability == Abilities.STR:
				self.str += amount
			elif ability == Abilities.DEX:
				self.dex += amount
			elif ability == Abilities.CON:
				self.con += amount
			elif ability == Abilities.INT:
				self.int += amount
			elif ability == Abilities.WIS:
				self.wis += amount
			elif ability == Abilities.CHA:
				self.cha += amount

	def addSkills(self, new_skills):
		self.skills +=new_skills

	def output(self):
		if self.subrace:
			print("{} {} {}".format(self.subrace.value, self.char_race.value, self.char_class.value))
		else:
			print("{} {}".format(self.char_race.value, self.char_class.value))
		outputLineBreak()
		print("{}: \t{} ({})".format(Abilities.STR.value, self.str, calculateModifier(self.str)))
		print("{}: \t{} ({})".format(Abilities.DEX.value, self.dex, calculateModifier(self.dex)))
		print("{}: \t{} ({})".format(Abilities.CON.value, self.con, calculateModifier(self.con)))
		print("{}: \t{} ({})".format(Abilities.INT.value, self.int, calculateModifier(self.int)))
		print("{}: \t{} ({})".format(Abilities.WIS.value, self.wis, calculateModifier(self.wis)))
		print("{}: \t{} ({})".format(Abilities.CHA.value, self.cha, calculateModifier(self.cha)))
		print("HP: \t\t{}".format(self.class_data["hit_die"] + calculateModifier(self.con)))
		print()
		print("Speed: \t\t{}".format(self.race_data["speed"]))
		print("Languages:")
		print(listToTabbedString(self.languages, 2))
		print("Proficiencies")
		outputLineBreak()
		print("Saving throws:")
		print(listToTabbedString([a.value for a in self.class_data["saving_throws"]], 2))
		print("Weapons:")
		print(listToTabbedString(self.class_data["weapon_proficiencies"], 2))
		print("Armour:")
		print(listToTabbedString(self.class_data["armour_proficiencies"], 2))
		print("Skills:")
		print(listToTabbedString([s.value for s in self.skills], 2))

def calculateModifier(score):
	return (score - 10)//2

def listToTabbedString(l, numTabs):
	s = ""
	for entry in l:
		for i in range(numTabs):
			s += "\t"
		s += entry
		s += "\n"
	return s

def outputLineBreak():
	print("----------------")