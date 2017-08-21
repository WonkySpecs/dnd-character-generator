from enum import Enum, auto

class AbilityRollMethod(Enum):
	FOUR_D6_DROP_LOWEST = "4d6 drop lowest"
	THREE_D6			= "3d6"
	D20 				= "d20 (Warning: Mad)"

	IN_ORDER 			= "In order"
	PICK_ORDER			= "Pick order"

class Races(Enum):
	DWARF		= "Dwarf"
	ELF			= "Elf"
	HALFLING	= "Halfling"
	HUMAN		= "Human"
	DRAGONBORN	= "DragonBorn"
	GNOME		= "Gnome"
	HALF_ELF	= "Half-elf"
	HALF_ORC	= "Half-orc"
	TIEFLING	= "Tiefling"

class Subraces(Enum):
	HILL		= "Hill"
	MOUNTAIN	= "Mountain"
	HIGH		= "High"
	WOOD		= "Wood"
	DARK		= "Dark"

class Classes(Enum):
	BARBARIAN	= "Barbarian"
	BARD		= "Bard"
	CLERIC		= "Cleric"
	DRUID		= "Druid"
	FIGHTER		= "Fighter"
	MONK		= "Monk"
	PALADIN		= "Paladin"
	RANGER		= "Ranger"
	ROGUE		= "Rogue"
	SORCERER	= "Sorcerer"
	WARLOCK		= "Warlock"
	WIZARD		= "Wizard"

class Abilities(Enum):
	STR	= "Strength"
	DEX = "Dexterity"
	CON = "Constitution"
	INT = "Intelligence"
	WIS = "Wisdow"
	CHA = "Charisma"

class Skills(Enum):
	ATHLETICS		= "Athletics"
	ACROBATICS		= "Acrobatics"
	SLEIGHT			= "Sleight of hand"
	STEALTH			= "Stealth"
	ARCANA			= "Arcana"
	HISTORY			= "History"
	INVESTIGATION	= "Investigation"
	NATURE			= "Nature"
	RELIGION		= "Religion"
	ANIMAL			= "Animal handling"
	INSIGHT			= "Insight"
	MEDICINE		= "Medicine"
	PERCEPTION		= "Perception"
	SURVIVAL		= "Surivival"
	DECEPTION		= "Deception"
	INTIMIDATION	= "Intimidation"
	PERFORMANCE		= "Performance"
	PERSUASION		= "Persuasion"

attr_skill_dict = { Abilities.STR : {Skills.ATHLETICS},

					Abilities.DEX : {Skills.ACROBATICS,
									 Skills.SLEIGHT,
									 Skills.STEALTH},

					Abilities.CON : {},

					Abilities.INT : {Skills.ARCANA,
									 Skills.HISTORY,
									 Skills.INVESTIGATION,
									 Skills.NATURE,
									 Skills.RELIGION},

					Abilities.WIS : {Skills.ANIMAL,
									 Skills.INSIGHT,
									 Skills.MEDICINE,
									 Skills.PERCEPTION,
									 Skills.SURVIVAL},

					Abilities.CHA : {Skills.DECEPTION,
									 Skills.INTIMIDATION,
									 Skills.PERFORMANCE,
									 Skills.PERSUASION}}

simple_melee_weapons = { "Club",
						 "Dagger", 
						 "Greatclub",
						 "Handaxe",
						 "Javelin",
						 "Light Hammer",
						 "Mace",
						 "Quarterstaff",
						 "Sickle",
						 "Spear"}

simple_ranged_weapons = { "Light crossbow",
						  "Dart", 
						  "Shortbow",
						  "Sling"}

class_data_dict	= {	Classes.BARBARIAN:
					{"hit_die"				: 12,
					 "prim_att"				: Abilities.CON,
	 				 "sec_att"				: Abilities.STR,
					 "weapon_proficiencies" : { "all"},
					 "armour_proficiencies" : { "light",
					 							"medium",
					 							"shields"},
					 "saving throws"		: { Abilities.STR,
											  	Abilities.CON}},
	
					Classes.BARD:
					{"hit_die"				: 8,
					 "prim_att"				: Abilities.CHA,
	 				 "sec_att"				: Abilities.DEX,
					 "weapon_proficiencies" : {"simple",
					 							"hand crossbows",
					 							"longswords",
					 							"rapiers",
					 							"shortswords"},
					 "armour_proficiencies" : { "light"},
					 "saving throws"		: { Abilities.CHA,
											  	Abilities.DEX}},

					Classes.CLERIC:
					{"hit_die"				: 8,
					 "prim_att"				: Abilities.WIS,
	 				 "sec_att"				: Abilities.CON,
					 "weapon_proficiencies" : {"simple"},
					 "armour_proficiencies" : { "light",
					 							"medium",
					 							"shields"},
					 "saving throws"		: { Abilities.WIS,
											  	Abilities.CHA}},
					Classes.DRUID:
					{"hit_die"				: 8,
					 "prim_att"				: Abilities.WIS,
	 				 "sec_att"				: Abilities.CON,
					 "weapon_proficiencies" : { "club",
												"daggers",
												"darts",
												"javelins",
												"maces",
												"quarterstaffs",
												"scimitars",
												"sickles",
												"slings",
												"spears"},
					 "armour_proficiencies" : { "light",
					 							"medium",
					 							"shields"},
					 "saving throws"		: { Abilities.INT,
											  	Abilities.WIS}}}

race_data_dict	= { Races.DWARF:
					{"languages"			: { "Common",
												"Dwarvish"},
					 "speed"				: 25,
					 "ability_increases"	: { Abilities.CON : 2},
					 "subraces"				: { Subraces.HILL,
					 							Subraces.MOUNTAIN}},
					Races.ELF:
					{"languages"			: { "Common",
												"Elvish"},
					 "speed"				: 30,
					 "ability_increases"	: { Abilities.DEX : 2},
					 "subraces"				: { Subraces.WOOD,
					 							Subraces.HIGH,
					 							Subraces.DARK}}}

subrace_data_dict = { Subraces.HILL:
						{"ability_increases"	: {Abilities.WIS : 1}
						},

					  Subraces.MOUNTAIN:
					  	{"ability_increases"	: {Abilities.STR : 2}},

					  Subraces.HIGH:
					  	{"ability_increases"	: {Abilities.INT : 1}},

					  Subraces.WOOD:
					  	{"ability_increases"	: {Abilities.WIS : 1}},

					  Subraces.DARK:
					  	{"ability_increases"	: {Abilities.CHA : 1}}}