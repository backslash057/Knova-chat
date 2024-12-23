import tkinter as tk 

from . import utils

class Groupbar(tk.Frame):
	def __init__(self, master, togglebar=None):
		super().__init__(master)
		self.pack_propagate(False)
		self.config(width=108, bg="#293A4C")

		self.togglebar = togglebar

		self.add_widgets()

	def add_widgets(self):
		self.hamb_icon = utils.load_image("hamburger.png")
		self.hamburger = tk.Canvas(self, width=70, height=70, highlightthickness=0, cursor="hand2")
		self.hamburger.config(bg=self.cget("bg"))
		self.hamburger.pack()
		self.hamburger.create_image(35, 35, image=self.hamb_icon)
		self.hamburger.bind("<Button-1>", lambda *args: self.togglebar())
