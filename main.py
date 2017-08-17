import random
from data_and_enums import *

def generateCharacter(races, classes, abilityScoreOrder = AbilityRollMethod.PICK_ORDER, abilityRollMethod = AbilityRollMethod.FOUR_D6_DROP_LOWEST):
	race_choice = random.sample(races, 1)[0]
	class_choice = random.sample(classes, 1)[0]

	class_data = class_data_dict[class_choice]
	race_data = race_data_dict[race_choice]

	pick_order = getPickOrder("normal", class_data)

	(strength, dexterity, constitution, intelligence, wisdom, charisma) = rollAbilityScores(abilityScoreOrder, abilityRollMethod, preference_order = pick_order)
	ability_scores = (strength, dexterity, constitution, intelligence, wisdom, charisma)
	print(ability_scores)

def rollAbilityScores(method, roll_method, preference_order = None):
	if method == AbilityRollMethod.IN_ORDER:
		return tuple([rollOneAbilityScore(roll_method) for i in range(6)])

	elif method == AbilityRollMethod.PICK_ORDER:
		if preference_order:
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

def getPickOrder(method, class_data):
	if method == "normal":
		pick_order = [class_data["prim_att"], class_data["sec_att"]]
		abilities = [a for a in Abilities]
		abilities.remove(class_data["prim_att"])
		abilities.remove(class_data["sec_att"])
		random.shuffle(abilities)
		return pick_order + abilities

generateCharacter({Races.DWARF}, {Classes.BARBARIAN})