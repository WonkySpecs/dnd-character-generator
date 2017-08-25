import random
from data_and_enums import *

def generateCharacter(races, classes, subraces = "all",
						abilityScoreOrderMethod = AbilityRollMethod.PICK_ORDER,
						abilityRollMethod = AbilityRollMethod.FOUR_D6_DROP_LOWEST,
						abilityScoreOrder = "classic"):
	race_choice = random.sample(races, 1)[0]
	class_choice = random.sample(classes, 1)[0]

	if(subraces == "all"):
		subrace_choice = random.sample(race_data_dict[race_choice]["subraces"], 1)[0]
	else:
		applicable_subraces = race_data_dict[race_choice]["subraces"]
		sr = [subrace for subrace in applicable_subraces if subrace in subraces]

		if sr:
			subrace_choice = random.sample(sr, 1)[0]
		else:
			subrace_choice = None

	class_data = class_data_dict[class_choice]
	race_data = race_data_dict[race_choice]
	if subrace_choice:
		subrace_data = subrace_data_dict[subrace_choice]

	pick_order = getPickOrder(abilityScoreOrder, class_data)

	(strength, dexterity, constitution, intelligence, wisdom, charisma) = rollAbilityScores(abilityScoreOrderMethod, abilityRollMethod, preference_order = pick_order)
	ability_scores = (strength, dexterity, constitution, intelligence, wisdom, charisma)
	ability_scores = applyAbilityIncreases(list(ability_scores), race_data["ability_increases"])

	if subrace_choice:
		ability_scores = applyAbilityIncreases(list(ability_scores), subrace_data["ability_increases"])
	skills = random.sample(class_data["skills"], class_data["num_skills"])
	outputCharacter(subrace_choice, race_choice, class_choice, race_data, class_data, ability_scores, skills)

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

def calculateModifier(score):
	return (score - 10)//2

# Takes list of ints in order of
# str, dex, con, int, wis, cha
# and a dict of {Abilities : int} and applies
# the increases to the appropriate ability
def applyAbilityIncreases(ability_list, increases):
	for ability in increases:
		amount = increases[ability]
		if ability == Abilities.STR:
			ability_list[0] += amount
		elif ability == Abilities.DEX:
			ability_list[1] += amount
		elif ability == Abilities.CON:
			ability_list[2] += amount
		elif ability == Abilities.INT:
			ability_list[3] += amount
		elif ability == Abilities.WIS:
			ability_list[4] += amount
		elif ability == Abilities.CHA:
			ability_list[5] += amount

	return tuple(ability_list)

# Takes either:
#	1. A strong defining the method for generating or
#	2. A list of up to 6 Abilities
# and outputs a list defining the preference for ability
# scores, most preffered first.
def getPickOrder(method, class_data):
	if method == "classic":
		pick_order = [class_data["prim_att"], class_data["sec_att"]]
	elif method == "random":
		pick_order = [a for a in Abilities]
		pick_order.shuffle()
		return pick_order
	else:
		pick_order = method

	abilities = [a for a in Abilities]
	for ability in pick_order:
		abilities.remove(ability)
	random.shuffle(abilities)
	return pick_order + abilities

def outputCharacter(subrace_choice, race_choice, class_choice, race_data, class_data, ability_scores, skills):
	if subrace_choice:
		print("{} {} {}".format(subrace_choice.value, race_choice.value, class_choice.value))
	else:
		print("{} {}".format(race_choice.value, class_choice.value))
	outputLineBreak()
	print("{}: \t{} ({})".format(Abilities.STR.value, ability_scores[0], calculateModifier(ability_scores[0])))
	print("{}: \t{} ({})".format(Abilities.DEX.value, ability_scores[1], calculateModifier(ability_scores[1])))
	print("{}: \t{} ({})".format(Abilities.CON.value, ability_scores[2], calculateModifier(ability_scores[2])))
	print("{}: \t{} ({})".format(Abilities.INT.value, ability_scores[3], calculateModifier(ability_scores[3])))
	print("{}: \t{} ({})".format(Abilities.WIS.value, ability_scores[4], calculateModifier(ability_scores[4])))
	print("{}: \t{} ({})".format(Abilities.CHA.value, ability_scores[5], calculateModifier(ability_scores[5])))
	print("HP: \t\t{}".format(class_data["hit_die"] + calculateModifier(ability_scores[2])))
	print()
	print("Speed: \t\t{}".format(race_data["speed"]))
	print("Languages:")
	print(listToTabbedString(race_data["languages"], 2))
	print("Proficiencies")
	outputLineBreak()
	print("Saving throws:")
	print(listToTabbedString([a.value for a in class_data["saving_throws"]], 2))
	print("Weapons:")
	print(listToTabbedString(class_data["weapon_proficiencies"], 2))
	print("Armour:")
	print(listToTabbedString(class_data["armour_proficiencies"], 2))
	print("Skills:")
	print(listToTabbedString([s.value for s in skills], 2))

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

def runTests():
	assert(calculateModifier(1) == -5)
	assert(calculateModifier(3) == -4)
	assert(calculateModifier(10) == 0)
	assert(calculateModifier(30) == 10)
	for i in range(100):
		assert(rollOneAbilityScore(AbilityRollMethod.FOUR_D6_DROP_LOWEST) in range(3, 18))
		assert(rollOneAbilityScore(AbilityRollMethod.THREE_D6) in range(3, 18))
		assert(rollOneAbilityScore(AbilityRollMethod.D20) in range(1, 20))
	po = getPickOrder("random", None)
	for ability in Abilities:
		assert(ability in po)

generateCharacter({Races.DWARF}, {Classes.BARBARIAN}, abilityRollMethod = AbilityRollMethod.STANDARD_ARRAY)
outputLineBreak()
outputLineBreak()
generateCharacter({Races.ELF}, {Classes.BARD}, {Subraces.DARK, Subraces.HIGH})
generateCharacter({r for r  in Races}, {c for c in class_data_dict.keys()}, {sr for sr in Subraces})