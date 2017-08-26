from enum import Enum, auto

class AbilityRollMethod(Enum):
	FOUR_D6_DROP_LOWEST = "4d6 drop lowest"
	THREE_D6			= "3d6"
	D20 				= "d20 (Warning: Mad)"

	STANDARD_ARRAY		= "Standard Array"

	IN_ORDER 			= "In order"
	PICK_ORDER			= "Pick order"

class Races(Enum):
	DWARF		= "Dwarf"
	ELF			= "Elf"
	HALFLING	= "Halfling"
	HUMAN		= "Human"
	DRAGONBORN	= "Dragonborn"
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
	LIGHTFOOT 	= "Lightfoot"
	STOUT		= "Stout"
	FOREST  	= "Forest"
	ROCK		= "Rock"

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
	WIS = "Wisdom"
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
					 "saving_throws"		: { Abilities.STR,
											  	Abilities.CON},
					 "skills"				: { Skills.ANIMAL,
					  							Skills.ATHLETICS,
					  							Skills.INTIMIDATION,
					  							Skills.NATURE,
					  							Skills.PERCEPTION,
					  							Skills.SURVIVAL},
					 "num_skills"			: 2},
	
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
					 "saving_throws"		: { Abilities.CHA,
											  	Abilities.DEX},
					 "skills"				: { s for s in Skills},
					 "num_skills"			: 3},

					Classes.CLERIC:
					{"hit_die"				: 8,
					 "prim_att"				: Abilities.WIS,
	 				 "sec_att"				: Abilities.CON,
					 "weapon_proficiencies" : {"simple"},
					 "armour_proficiencies" : { "light",
					 							"medium",
					 							"shields"},
					 "saving_throws"		: { Abilities.WIS,
											  	Abilities.CHA},
					 "skills"				: { Skills.HISTORY,
					 							Skills.INSIGHT,
					 							Skills.MEDICINE,
					 							Skills.PERSUASION,
					 							Skills.RELIGION},
					 "num_skills"			: 2},

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
					 "saving_throws"		: { Abilities.INT,
											  	Abilities.WIS},
					 "skills"				: { Skills.ANIMAL,
					 							Skills.INSIGHT,
					 							Skills.MEDICINE,
					 							Skills.NATURE,
					 							Skills.RELIGION,
					 							Skills.PERCEPTION,
					 							Skills.SURVIVAL},
					 "num_skills"			: 2 },

					Classes.FIGHTER:
					{"hit_die"				: 10,
					 "prim_att"				: Abilities.STR,
	 				 "sec_att"				: Abilities.CON,
					 "weapon_proficiencies" : { "all"},
					 "armour_proficiencies" : { "all",
					 							"shields"},
					 "saving_throws"		: { Abilities.STR,
											  	Abilities.CON},
					 "skills"				: { Skills.ACROBATICS,
					 							Skills.ANIMAL,
					 							Skills.ATHLETICS,
					 							Skills.HISTORY,
					 							Skills.INSIGHT,
					 							Skills.INTIMIDATION,
					 							Skills.PERCEPTION,
					 							Skills.SURVIVAL},
					 "num_skills"			: 2 },

					Classes.MONK:
					{"hit_die"				: 8,
					 "prim_att"				: Abilities.DEX,
	 				 "sec_att"				: Abilities.WIS,
					 "weapon_proficiencies" : { "simple",
					 							"shortswords"},
					 "armour_proficiencies" : { },
					 "saving_throws"		: { Abilities.STR,
											  	Abilities.DEX},
					 "skills"				: { Skills.ACROBATICS,
					 							Skills.ATHLETICS,
					 							Skills.HISTORY,
					 							Skills.RELIGION,
					 							Skills.STEALTH},
					 "num_skills"			: 2 },

					Classes.PALADIN:
					{"hit_die"				: 10,
					 "prim_att"				: Abilities.STR,
	 				 "sec_att"				: Abilities.CHA,
					 "weapon_proficiencies" : { "all"},
					 "armour_proficiencies" : { "all",
					 							"shields"},
					 "saving_throws"		: { Abilities.WIS,
											  	Abilities.CHA},
					 "skills"				: { Skills.ATHLETICS,
												Skills.INSIGHT,
												Skills.INTIMIDATION,
												Skills.MEDICINE,
					 							Skills.PERSUASION,
					 							Skills.RELIGION},
					 "num_skills"			: 2 },

					Classes.RANGER:
					{"hit_die"				: 10,
					 "prim_att"				: Abilities.DEX,
	 				 "sec_att"				: Abilities.WIS,
					 "weapon_proficiencies" : { "all"},
					 "armour_proficiencies" : { "light",
					 							"medium",
					 							"shields"},
					 "saving_throws"		: { Abilities.STR,
											  	Abilities.DEX},
					 "skills"				: { Skills.ANIMAL,
												Skills.ATHLETICS,
												Skills.INSIGHT,
												Skills.INVESTIGATION,
												Skills.NATURE,
					 							Skills.PERCEPTION,
					 							Skills.STEALTH,
					 							Skills.SURVIVAL},
					 "num_skills"			: 3 },

					Classes.ROGUE:
					{"hit_die"				: 8,
					 "prim_att"				: Abilities.DEX,
	 				 "sec_att"				: Abilities.CHA,
					 "weapon_proficiencies" : { "simple",
					 							"hand crossbows",
					 							"longswords",
					 							"rapiers",
					 							"shortswords"},
					 "armour_proficiencies" : { "light"},
					 "saving_throws"		: { Abilities.INT,
											  	Abilities.DEX},
					 "skills"				: { Skills.ACROBATICS,
												Skills.ATHLETICS,
												Skills.DECEPTION,
												Skills.INSIGHT,
												Skills.INTIMIDATION,
												Skills.INVESTIGATION,
					 							Skills.PERCEPTION,
												Skills.PERFORMANCE,
												Skills.PERSUASION,
					 							Skills.SLEIGHT,
					 							Skills.STEALTH},
					 "num_skills"			: 4 },

					Classes.SORCERER:
					{"hit_die"				: 6,
					 "prim_att"				: Abilities.CHA,
	 				 "sec_att"				: Abilities.CON,
					 "weapon_proficiencies" : { "daggers",
					 							"darts",
					 							"slings",
					 							"quarterstaffs",
					 							"light crossbows"},
					 "armour_proficiencies" : { },
					 "saving_throws"		: { Abilities.CON,
											  	Abilities.CHA},
					 "skills"				: { Skills.ARCANA,
												Skills.DECEPTION,
												Skills.INSIGHT,
												Skills.INTIMIDATION,
												Skills.PERSUASION,
					 							Skills.RELIGION},
					 "num_skills"			: 2 },

					Classes.WARLOCK:
					{"hit_die"				: 8,
					 "prim_att"				: Abilities.CHA,
	 				 "sec_att"				: Abilities.CON,
					 "weapon_proficiencies" : { "simple"},
					 "armour_proficiencies" : { "light"},
					 "saving_throws"		: { Abilities.WIS,
											  	Abilities.CHA},
					 "skills"				: { Skills.ARCANA,
												Skills.DECEPTION,
												Skills.HISTORY,
												Skills.INTIMIDATION,
												Skills.INVESTIGATION,
												Skills.NATURE,
					 							Skills.RELIGION},
					 "num_skills"			: 2 },

					Classes.WIZARD:
					{"hit_die"				: 6,
					 "prim_att"				: Abilities.INT,
	 				 "sec_att"				: Abilities.CON,
					 "weapon_proficiencies" : { "daggers",
					 							"darts",
					 							"slings",
					 							"quarterstaffs",
					 							"light crossbows"},
					 "armour_proficiencies" : { },
					 "saving_throws"		: { Abilities.INT,
											  	Abilities.WIS},
					 "skills"				: { Skills.ARCANA,
												Skills.HISTORY,
												Skills.INSIGHT,
												Skills.INVESTIGATION,
												Skills.MEDICINE,
					 							Skills.RELIGION},
					 "num_skills"			: 2 }}

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
						 							Subraces.DARK}},
					Races.HALFLING:
						{"languages"			: { "Common",
													"Halfling"},
						 "speed"				: 25,
						 "ability_increases"	: { Abilities.DEX : 2},
						 "subraces"				: { Subraces.STOUT,
						 							Subraces.LIGHTFOOT}},
	
					Races.HUMAN:
						{"languages"			: { "Common"},
						 "optional_languages"	: {},
						 "speed"				: 30,
						 "ability_increases"	: { Abilities.STR : 1,
						 							Abilities.DEX : 1,
						 							Abilities.CON : 1,
						 							Abilities.INT : 1,
						 							Abilities.WIS : 1,
						 							Abilities.CHA : 1},
						 "subraces"				: {}},
	
					Races.DRAGONBORN:
						{"languages"			: { "Common",
													"Draconic"},
						 "speed"				: 30,
						 "ability_increases"	: { Abilities.STR : 2,
						 							Abilities.CHA : 1},
						 "subraces"				: {}},
	
					Races.GNOME:
						{"languages"			: { "Common",
													"Gnomish"},
						 "speed"				: 25,
						 "ability_increases"	: { Abilities.INT : 2},
						 "subraces"				: { Subraces.FOREST,
						 							Subraces.ROCK}},
	
					Races.HALF_ELF:
						{"languages"			: { "Common",
													"Elvish"},
						 "optional_languages"	: {},
						 "speed"				: 30,
						 "ability_increases"	: { Abilities.CHA : 2},
						 "subraces"				: {}},
	
					Races.HALF_ORC:
						{"languages"			: { "Common",
													"Orc"},
						 "speed"				: 30,
						 "ability_increases"	: { Abilities.CON : 1,
						 							Abilities.STR : 2},
						 "subraces"				: {}},
	
					Races.TIEFLING:
						{"languages"			: { "Common",
													"Infernal"},
						 "speed"				: 30,
						 "ability_increases"	: { Abilities.CHA : 2,
						 							Abilities.INT : 1},
						 "subraces"				: {}}}

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
					  	{"ability_increases"	: {Abilities.CHA : 1}},

					  Subraces.LIGHTFOOT:
					  	{"ability_increases"	: {Abilities.CHA : 1}},

					  Subraces.STOUT:
					  	{"ability_increases"	: {Abilities.CON : 1}},

					  Subraces.FOREST:
					  	{"ability_increases"	:{ Abilities.DEX : 1}},

					  Subraces.ROCK:
					  	{"ability_increases"	:{ Abilities.CON : 1}}}