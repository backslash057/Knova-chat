import tkinter as tk

from . import utils

class Chatzone(tk.Canvas):
	def __init__(self, master, configs, mode):
		super().__init__(master)
		self.configs=configs
		self.mode = mode
		self.config(highlightthickness=0)

		self.update_mode()
	

	def update_mode(self, mode=None):
		if mode: self.mode = mode

		self.config(bg=self.configs['.'][self.mode])

