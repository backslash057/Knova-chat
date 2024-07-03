import tkinter as tk
import tkinter.font as tkFont

from . import utils

class Messagebar(tk.Frame):
	def __init__(self, master, configs, mode):
		super().__init__(master)
		self.configs=configs
		self.mode=mode

		self.config(height=70, highlightthickness=1)
		self.pack_propagate(False)

		self.pin = tk.Canvas(self, width=70, bg="#ffffff", highlightthickness=0, cursor="hand2")
		self.pin.pack(side="left", fill="y")
		self.pin.bind("<Button-1>", self.sendmedia)
		self.pin_icon = utils.load_image("pin.png")
		self.pin.create_image(35, 35, image=self.pin_icon)


		font = tkFont.Font(family="Calibri", size=11)
		self.entry = tk.Text(self, font=font, relief="flat", height=1)
		self.entry.pack(side="left", fill="x", expand=True)


		self.emoji = tk.Canvas(self, width=70, highlightthickness=0, cursor="hand2")
		self.emoji.pack(side="right")
		self.emoji.bind("<Button-1>", self.display_emojis)
		self.emoji_icon = utils.load_image("emoji.png")
		self.emoji.create_image(35, 35, image=self.emoji_icon)

		self.microphone = tk.Canvas(self, width=70, highlightthickness=0, cursor="hand2")
		self.microphone.pack(side="right", before=self.emoji)
		self.microphone.bind("<Button-1>", self.start_microphone)
		self.microphone_icon = utils.load_image("microphone.png")
		self.microphone.create_image(35, 35, image=self.microphone_icon)

		self.update_mode()

	def sendmedia(self):
		pass

	def display_emojis(self):
		pass

	def start_microphone(self):
		pass

	def update_mode(self, mode=None):
		if mode: self.mode=mode

		self.config(bg=self.configs['.'][self.mode])
		self.config(highlightbackground=self.configs['border'][self.mode])
		self.config(highlightcolor=self.configs['border'][self.mode])
		self.pin.config(bg=self.configs['pin'][self.mode])
		self.entry.config(bg=self.configs['entry']['bg'][self.mode])
		self.entry.config(fg=self.configs['entry']['fg'][self.mode])
		self.emoji.config(bg=self.configs['emoji'][self.mode])
		self.microphone.config(bg=self.configs['microphone'][self.mode])
