import random
from data_and_enums import *

def generateCharacter(races, classes, subraces = "all", abilityScoreOrder = AbilityRollMethod.PICK_ORDER, abilityRollMethod = AbilityRollMethod.FOUR_D6_DROP_LOWEST):
	race_choice = random.sample(races, 1)[0]
	class_choice = random.sample(classes, 1)[0]

	if(subraces == "all"):
		subrace_choice = random.sample(race_data_dict[race_choice]["subraces"], 1)[0]
	else:
		applicable_subraces = race_data_dict[race_choice]["subraces"]
		sr = [subrace for subrace in applicable_subraces if subrace in subraces]
		subrace_choice = random.sample(sr, 1)[0]	

	class_data = class_data_dict[class_choice]
	race_data = race_data_dict[race_choice]
	subrace_data = subrace_data_dict[subrace_choice]

	pick_order = getPickOrder("normal", class_data)

	(strength, dexterity, constitution, intelligence, wisdom, charisma) = rollAbilityScores(abilityScoreOrder, abilityRollMethod, preference_order = pick_order)
	ability_scores = (strength, dexterity, constitution, intelligence, wisdom, charisma)
	ability_scores = applyAbilityIncreases(list(ability_scores), race_data["ability_increases"])
	ability_scores = applyAbilityIncreases(list(ability_scores), subrace_data["ability_increases"])
	outputCharacter(subrace_choice, race_choice, class_choice, race_data, ability_scores)

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

def getPickOrder(method, class_data):
	if method == "normal":
		pick_order = [class_data["prim_att"], class_data["sec_att"]]
		abilities = [a for a in Abilities]
		abilities.remove(class_data["prim_att"])
		abilities.remove(class_data["sec_att"])
		random.shuffle(abilities)
		return pick_order + abilities

def outputCharacter(subrace_choice, race_choice, class_choice, race_data, ability_scores):
	print("{} {} {}".format(subrace_choice.value, race_choice.value, class_choice.value))
	print("{}: \t{} ({})".format(Abilities.STR.value, ability_scores[0], calculateModifier(ability_scores[0])))
	print("{}: \t{} ({})".format(Abilities.DEX.value, ability_scores[1], calculateModifier(ability_scores[1])))
	print("{}: \t{} ({})".format(Abilities.CON.value, ability_scores[2], calculateModifier(ability_scores[2])))
	print("{}: \t{} ({})".format(Abilities.INT.value, ability_scores[3], calculateModifier(ability_scores[3])))
	print("{}: \t{} ({})".format(Abilities.WIS.value, ability_scores[4], calculateModifier(ability_scores[4])))
	print("{}: \t{} ({})".format(Abilities.CHA.value, ability_scores[5], calculateModifier(ability_scores[5])))
	print("Speed: {}".format(race_data["speed"]))

generateCharacter({Races.DWARF}, {Classes.BARBARIAN}, abilityRollMethod = AbilityRollMethod.STANDARD_ARRAY)
print("---------------------------------")
generateCharacter({Races.ELF}, {Classes.BARD}, {Subraces.DARK, Subraces.HIGH})