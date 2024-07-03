import tkinter as tk
import tkinter.font as tkFont

from . import utils


class Chatlabel(tk.Frame):
	def __init__(self, master, configs, mode, icon, name, text):
		super().__init__(master)
		self.configs=configs
		self.mode = mode
		self.status="normal"

		self.config(height=90, padx=10, pady=10)
		self.pack_propagate(False)

		self.icon = utils.load_image(icon, (60, 60))
		self.logo = tk.Canvas(self, width=60, height=60, highlightthickness=0)
		self.logo.pack(side="left")
		self.logo.create_image(30, 30, image=self.icon)

		self.container = tk.Frame(self)
		self.container.pack(side="left", padx=(20, 0))

		namefont= tkFont.Font(family="Calibri", size=12, weight="bold")
		self.name = tk.Label(self.container, text=name, font=namefont)
		self.name.pack(anchor="w")

		if len(text)>=20: text=text[:20]
		self.text = tk.Label(self.container, text=text)
		self.text.pack(pady=(10, 0), anchor="w")


		self.bind("<Enter>", lambda *args: self.hover("hovered"))
		self.bind("<Leave>", lambda *args: self.hover("normal"))

		self.update_mode()

	def hover(self, state):
		self.status = state
		self.update_mode()


	def update_mode(self, mode=None):
		if mode: self.mode = mode

		self.config(bg=self.configs[self.status]['.'][self.mode])
		self.logo.config(bg=self.configs[self.status]['logo'][self.mode])

		self.container.config(bg=self.configs[self.status]['container']['.'][self.mode])
		self.name.config(bg=self.configs[self.status]['container']['name']['bg'][self.mode])
		self.name.config(fg=self.configs[self.status]['container']['name']['fg'][self.mode])
		self.text.config(bg=self.configs[self.status]['container']['text']['bg'][self.mode])
		self.text.config(fg=self.configs[self.status]['container']['text']['fg'][self.mode])


class Searchbar(tk.Canvas):
	def __init__(self, master, configs, mode):
		super().__init__(master)
		self.pack_propagate(False)
		self.config(bg="#fff", height=80, highlightthickness=0)
		self.configs = configs
		self.mode = mode

		font = tkFont.Font(family="Calibri", size=11)
		self.entry = tk.Entry(self, bg="#f1f1f1", relief="flat", font=font, width=26)

		self.add_entry()
		self.add_active_entry()

	def add_entry(self):
		self.create_window(180, 40, window=self.entry)

		swidth = 24
		width, height = 280, 31
		padx, pady = 10, 10
		posx, posy = 40, 25
		dia = height + 2*pady

		self.rect = self.create_rectangle((posx, posy-pady-1, posx+width+swidth, posy+height+pady+1), fill="#f1f1f1", outline="")
		self.arc_left = self.create_oval((posx-dia//2, posy-pady, posx+dia//2, posy+height+pady), fill="#f1f1f1", outline="")
		self.arc_right = self.create_oval((posx+swidth+width-dia//2, posy-pady-1, posx+swidth+width+dia//2, posy+height+pady), fill="#f1f1f1", outline="")

		self.update_mode()

	def add_active_entry(self):
		pass
		#self.delete("all")

	def update_mode(self, mode=None):
		if mode: self.mode = mode 

		self.config(bg=self.configs['.'][self.mode])

		self.itemconfig(self.arc_left, fill=self.configs['entry']['bg'][self.mode])
		self.itemconfig(self.rect, fill=self.configs['entry']['bg'][self.mode])
		self.entry.config(bg=self.configs['entry']['bg'][self.mode])
		self.entry.config(fg=self.configs['entry']['fg'][self.mode])
		self.itemconfig(self.arc_right, fill=self.configs['entry']['bg'][self.mode])
		

class Chatmenu(tk.Frame):
	def __init__(self, master, configs, mode):
		super().__init__(master)
		self.configs = configs
		self.mode = mode

		self.pack_propagate(False)
		self.config(width=390)

		self.searchbar = Searchbar(self, configs=self.configs['searchbar'], mode=self.mode)
		self.searchbar.pack(fill="x")

		self.chats=[]
		self.add_chats()
		self.update_mode()
		

	def add_chats(self):
		test = Chatlabel(self, self.configs['chat'], self.mode, "profile.png", "Ivana🌹", "Salut. je ne vois pas trop comment. en fait je suis entrain")
		test.pack(fill="x")

		test = Chatlabel(self, self.configs['chat'], self.mode, "profile.png", "Alias", "Mouf mon chaud petit. tu coirs dans le sac en bon mougou")
		test.pack(fill="x")

		test = Chatlabel(self, self.configs['chat'], self.mode, "profile.png", "dilane vignol", "je ne vois pas trop de quoi tu veux parler. soit plus clair")
		test.pack(fill="x")

		self.chats.append(test)

	def update_mode(self, mode=None):
		if mode:
			self.mode = mode
			self.searchbar.update_mode(self.mode)

		self.config(bg=self.configs['.'][self.mode])
		

		for chat in self.chats:
			chat.update_mode(self.mode)


