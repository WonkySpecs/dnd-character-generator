import random
import gui
from character import Character, calculateModifier
from data_and_enums import *

def generateCharacter(races, classes, subraces = "all",
						abilityScoreOrderMethod = AbilityRollMethod.PICK_ORDER,
						abilityRollMethod = AbilityRollMethod.FOUR_D6_DROP_LOWEST,
						abilityScoreOrder = "classic"):

	race_choice = random.sample(races, 1)[0]
	class_choice = random.sample(classes, 1)[0]

	if(subraces == "all"):
		if race_data_dict[race_choice]["subraces"]:
			subrace_choice = random.sample(race_data_dict[race_choice]["subraces"], 1)[0]
		else:
			subrace_choice = None
	else:
		applicable_subraces = race_data_dict[race_choice]["subraces"]
		sr = [subrace for subrace in applicable_subraces if subrace in subraces]

		if sr:
			subrace_choice = random.sample(sr, 1)[0]
		else:
			subrace_choice = None

	char = Character(race_choice, class_choice, subrace_choice)

	pick_order = getPickOrder(abilityScoreOrder, char.class_data)

	(strength, dexterity, constitution, intelligence, wisdom, charisma) = rollAbilityScores(abilityScoreOrderMethod, abilityRollMethod, preference_order = pick_order)
	char.setAbilityScores(strength, dexterity, constitution, intelligence, wisdom, charisma)
	char.applyAbilityIncreases(char.race_data["ability_increases"])
	if subrace_choice:
		ability_scores = char.applyAbilityIncreases(char.subrace_data["ability_increases"])

	skills = random.sample(char.class_data["skills"], char.class_data["num_skills"])
	char.addSkills(skills)
	return char

def rollAbilityScores(method, roll_method, preference_order = None):
	if method == AbilityRollMethod.IN_ORDER:
		return tuple([rollOneAbilityScore(roll_method) for i in range(6)])
	elif method == AbilityRollMethod.PICK_ORDER:
		if preference_order:
			if roll_method == AbilityRollMethod.STANDARD_ARRAY:
				rolls = [15, 14, 13, 12, 10, 8]
			else:
				rolls = [rollOneAbilityScore(roll_method) for i in range(6)]
			rolls.sort()
			rolls.reverse()
			strength = rolls[preference_order.index(Abilities.STR)]
			dexterity = rolls[preference_order.index(Abilities.DEX)]
			constitution = rolls[preference_order.index(Abilities.CON)]
			intelligence = rolls[preference_order.index(Abilities.INT)]
			wisdom = rolls[preference_order.index(Abilities.WIS)]
			charisma = rolls[preference_order.index(Abilities.CHA)]

			return (strength, dexterity, constitution, intelligence, wisdom, charisma)
		else:
			#If no order given, act like IN_ORDER
			return tuple([rollOneAbilityScore(roll_method) for i in range(6)])
	else:
		print("Invalid method passed to rollAbilityScore")

def rollOneAbilityScore(method):
	if method == AbilityRollMethod.FOUR_D6_DROP_LOWEST:
		rolls = [random.randint(1, 6) for i in range(4)]
		rolls.remove(min(rolls))
		return sum(rolls)

	elif method == AbilityRollMethod.THREE_D6:
		rolls = [random.randint(1, 6) for i in range(3)]
		return sum(rolls)
	elif method == AbilityRollMethod.D20:
		return random.randint(1, 20)
	else:
		print("Invalid method passed to rollOneAbilityScore")

# Takes either:
#	1. A string defining the method for generating or
#	2. A list of up to 6 Abilities
# and outputs a list defining the preference for ability
# scores, most preffered first.
def getPickOrder(method, class_data):
	if method == "classic":
		pick_order = [class_data["prim_att"], class_data["sec_att"]]
	elif method == "random":
		pick_order = [a for a in Abilities]
		random.shuffle(pick_order)
		return pick_order
	else:
		pick_order = method

	abilities = [a for a in Abilities]
	for ability in pick_order:
		abilities.remove(ability)
	random.shuffle(abilities)
	return pick_order + abilities

def outputLineBreak():
	print("----------------")

def runTests():
	assert(calculateModifier(1) == -5)
	assert(calculateModifier(3) == -4)
	assert(calculateModifier(10) == 0)
	assert(calculateModifier(30) == 10)
	for i in range(1000):
		assert(rollOneAbilityScore(AbilityRollMethod.FOUR_D6_DROP_LOWEST) in range(3, 19))
		assert(rollOneAbilityScore(AbilityRollMethod.THREE_D6) in range(3, 19))
		assert(rollOneAbilityScore(AbilityRollMethod.D20) in range(1, 21))
	po = getPickOrder("random", None)
	for ability in Abilities:
		assert(ability in po)

if __name__ == "__main__":
	runTests()
	root = gui.GUI()

	root.mainloop()
