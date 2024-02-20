import tkinter as tk 
import tkinter.font as tkFont

from . import utils

class Titlebar(tk.Frame):
	def __init__(self, master, configs, mode):
		super().__init__(master)
		self.pack_propagate(False)
		self.config(bg="#ffffff", height=80, highlightthickness=1, highlightbackground="#e7e7e7")
		self.configs = configs
		self.mode = mode

		self.container = tk.Frame(self)
		self.container.pack(side="left", padx=(20, 15))

		title_font = tkFont.Font(family="Roboto", size=10)
		self.chattitle = tk.Label(self.container, text="Ivana🌹", font=title_font)
		self.chattitle.pack(side="top", anchor="w")

		subtitle_font = tkFont.Font(family="Roboto", size=9, weight="normal")
		self.status = tk.Label(self.container, text="last seen too long ago :(", font=subtitle_font)
		self.status.pack(side="top", anchor="w")

		self.dots = tk.Canvas(self, width=70, highlightthickness=0, cursor="hand2")
		self.dots.pack(side="right")
		self.dots_icon = utils.load_image("3_dots.png")
		self.dots.create_image(35, 35, image=self.dots_icon)

		self.update_mode()

	def update_mode(self, mode=None):
		if mode: self.mode = mode

		self.config(bg=self.configs['.'][self.mode])
		self.config(highlightbackground=self.configs['border'][self.mode])
		self.container.config(bg=self.configs['container']['.'][self.mode])
		self.chattitle.config(bg=self.configs['container']['chattitle']['bg'][self.mode])
		self.chattitle.config(fg=self.configs['container']['chattitle']['fg'][self.mode])
		self.status.config(bg=self.configs['container']['status']['bg'][self.mode])
		self.status.config(fg=self.configs['container']['status']['fg'][self.mode])
		self.dots.config(bg=self.configs['dots'][self.mode])

