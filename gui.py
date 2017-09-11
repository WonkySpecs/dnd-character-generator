import tkinter as tk
from tkinter import ttk
from math import ceil
from data_and_enums import *

def setAllChecks(frame, value):
	print(value)
	for widget in frame.winfo_children():
		if widget.winfo_class() == "Checkbutton":
			if value == True:
				widget.select()
			else:
				widget.deselect()

class GUI(tk.Tk):
	def __init__(self):
		super(GUI, self).__init__()
		self.setUpClassSettingFrame()
		self.setUpRaceSettingFrame()
		self.setUpAbilityFrame()
		self.setUpFinalFrame()

		self.class_setting_frame.grid(row = 0, column = 0, sticky = tk.W  + tk.N)
		self.race_setting_frame.grid(row = 0, column = 1, sticky = tk.E + tk.N)
		self.ability_setting_frame.grid(row = 1, column = 0, sticky = tk.W  + tk.S)
		self.final_setting_frame.grid(row = 1, column = 1, sticky = tk.E + tk.S)

	def setUpClassSettingFrame(self):
		self.class_setting_frame = tk.LabelFrame(self, text = "Classes")

		self.class_boolean_var_dict = dict((c, tk.BooleanVar()) for c in Classes)
		for v in self.class_boolean_var_dict.values():
			v.set(True)
		self.class_check_dict = dict((tk.Checkbutton(self.class_setting_frame, text = c.value, var = self.class_boolean_var_dict[c]), c) for c in Classes)

		r = 0
		c= 0
		max_rows  = ceil(len(Classes) / 2)
		for check in self.class_check_dict.keys():
			check.grid(row = r, column = c, sticky = tk.W)
			r += 1
			if r >= max_rows:
				r = 0
				c = 1

		self.check_all_classes_button = tk.ttk.Button(self.class_setting_frame, text = "Check all", command = lambda : setAllChecks(self.class_setting_frame, True))
		self.uncheck_all_classes_button = tk.ttk.Button(self.class_setting_frame, text = "Uncheck all", command = lambda : setAllChecks(self.class_setting_frame, False))
		self.check_all_classes_button.grid(row = max_rows + 1, column = 0)
		self.uncheck_all_classes_button.grid(row = max_rows + 1, column = 1)

	def setUpRaceSettingFrame(self):
		self.race_setting_frame = tk.LabelFrame(self, text = "Races")

		self.race_boolean_var_dict = dict((c, tk.BooleanVar()) for c in Races)
		for v in self.race_boolean_var_dict.values():
			v.set(True)
		self.race_check_dict = dict((tk.Checkbutton(self.race_setting_frame, text = c.value, var = self.race_boolean_var_dict[c]), c) for c in Races)

		r = 0
		c= 0
		max_rows  = ceil(len(Races) / 2)
		for check in self.race_check_dict.keys():
			check.grid(row = r, column = c, sticky = tk.W)
			r += 1
			if r >= max_rows:
				r = 0
				c = 1

		self.check_all_racees_button = tk.ttk.Button(self.race_setting_frame, text = "Check all", command = lambda : setAllChecks(self.race_setting_frame, True))
		self.uncheck_all_racees_button = tk.ttk.Button(self.race_setting_frame, text = "Uncheck all", command = lambda : setAllChecks(self.race_setting_frame, False))
		self.check_all_racees_button.grid(row = max_rows + 1, column = 0)
		self.uncheck_all_racees_button.grid(row = max_rows + 1, column = 1)

	def setUpAbilityFrame(self):
		self.ability_setting_frame = tk.LabelFrame(self, text = "Ability priority")

		self.ability_mode = tk.StringVar()
		self.ability_mode.set("default")
		self.ability_mode.trace("w", self.toggleCustomAbilityModeEnabled)
		modes = [("Class default", "default"),
					("Custom", "custom")]

		r = 0
		for text, mode in modes:
			ability_radiobutton = tk.Radiobutton(self.ability_setting_frame, text = text, variable = self.ability_mode, value = mode)
			ability_radiobutton.grid(column = 0, row = r, sticky = tk.W)
			r += 1

		attribute_label = tk.Label(self.ability_setting_frame, text = "Attribute")
		priority_label = tk.Label(self.ability_setting_frame, text = "Priority")
		attribute_label.grid(column = 0, row = r)
		priority_label.grid(column = 1, row = r)
		r += 1

		self.ability_var_dict = dict((s, tk.IntVar()) for s in Abilities)
		self.ability_priority_menus = []

		for ability in Abilities:
			self.ability_var_dict[ability].set(1)
			drop_menu = tk.ttk.OptionMenu(self.ability_setting_frame, self.ability_var_dict[ability], None, 1, 2, 3, 4, 5, 6)
			drop_menu.configure(state = "disabled")
			self.ability_priority_menus.append(drop_menu)
			label = tk.Label(self.ability_setting_frame, text = ability.value)
			label.grid(column = 0, row = r)
			drop_menu.grid(column = 1, row = r, sticky = tk.E)
			r += 1

	def setUpFinalFrame(self):
		self.final_setting_frame = tk.Frame(self)
		self.unrestricted_char_button = tk.ttk.Button(self.final_setting_frame, text = "Create unrestricted character", command = lambda : self.collectOptionsAndCreateCharacter("unrestricted"))
		self.restricted_char_button = tk.ttk.Button(self.final_setting_frame, text = "Create \"sensible\" character", command = lambda : self.collectOptionsAndCreateCharacter("restricted"))
		self.unrestricted_char_button.grid(column = 0, row = 0)
		self.restricted_char_button.grid(column = 0, row = 1)

	def toggleCustomAbilityModeEnabled(self, *args):
		if self.ability_mode.get() == "default":
			for menu in self.ability_priority_menus:
				menu.configure(state = "disabled")
		else:
			for menu in self.ability_priority_menus:
				menu.configure(state = "active")

	def collectOptionsAndCreateCharacter(self, mode):
		print(mode)


if __name__ == "__main__":
	root = GUI()

	root.mainloop()