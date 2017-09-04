import tkinter as tk
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

		self.class_setting_frame.grid(row = 0, column = 0)
		self.race_setting_frame.grid(row = 0, column = 1)

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

		self.check_all_classes_button = tk.Button(self.class_setting_frame, text = "Check all", command = lambda : setAllChecks(self.class_setting_frame, True))
		self.uncheck_all_classes_button = tk.Button(self.class_setting_frame, text = "Uncheck all", command = lambda : setAllChecks(self.class_setting_frame, False))
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

		self.check_all_racees_button = tk.Button(self.race_setting_frame, text = "Check all", command = lambda : setAllChecks(self.race_setting_frame, True))
		self.uncheck_all_racees_button = tk.Button(self.race_setting_frame, text = "Uncheck all", command = lambda : setAllChecks(self.race_setting_frame, False))
		self.check_all_racees_button.grid(row = max_rows + 1, column = 0)
		self.uncheck_all_racees_button.grid(row = max_rows + 1, column = 1)




root = GUI()

root.mainloop()