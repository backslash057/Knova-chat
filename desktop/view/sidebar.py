import tkinter as tk
import tkinter.font as tkFont

from . import utils

class Toggle(tk.Canvas):
	def __init__(self, master, configs, mode, oncommand=None, offcommand=None):
		super().__init__(master)
		self.config(width=55, height=29, highlightthickness=0)

		self.oncommand = oncommand
		self.offcommand = offcommand
		self.configs=configs
		self.mode = mode

		self.value = "on" if self.mode=="dark" else "off"

		self.initial = (2, 1, 28, 27)
		self.final = (27, 1, 53, 27)

		self.arc_left = self.create_arc((2, 3, 24, 25), start=90, extent=180, outline="")
		self.rect = self.create_rectangle((13, 3, 38, 26), outline="")
		self.arc_right = self.create_arc((27, 3, 49, 25), start=-90, extent=180, outline="")

		pos = self.initial if self.value =="off" else self.final
		self.ball = self.create_oval(pos, width=4)

		self.bind("<Button-1>", self.toggle)
		self.update_mode()

	def toggle(self, event):
		self.unbind("<Button-1>")
		if self.value == "off":
			self.value = "on"
			self.right()
			
		elif self.value == "on":
			self.value = "off"
			self.left()
			

	def right(self):
		pos = self.coords(self.ball)
		if pos[0] < self.final[0]:
			dest = (min(pos[0]+6, self.final[0]), pos[1], min(pos[2]+6, self.final[2]), pos[3])
			self.coords(self.ball, dest)
			self.after(20, self.right)
		else:
			self.coords(self.ball, self.final)
			self.update_mode()
			self.bind("<Button-1>", self.toggle)
			if self.oncommand: self.oncommand()

	def left(self):
		pos = self.coords(self.ball)
		if pos[0] > self.initial[0]:
			dest = (max(pos[0]-6, self.initial[0]), pos[1], max(pos[2]-6, self.initial[2]), pos[3])
			self.move(self.ball, -6, 0)
			self.after(20, self.left)
		else:
			self.coords(self.ball, self.initial)
			self.update_mode()
			self.bind("<Button-1>", self.toggle)
			if self.offcommand: self.offcommand()

	def update_mode(self):
		self.mode = "light" if self.value=="off" else "dark"

		self.itemconfig(self.ball, outline=self.configs['ball']['outline'][self.mode], fill=self.configs['ball']['bg'][self.mode])
		self.itemconfig(self.arc_left, fill=self.configs['bg'][self.mode])
		self.itemconfig(self.rect, fill=self.configs['bg'][self.mode])
		self.itemconfig(self.arc_right, fill=self.configs['bg'][self.mode])


class SidebarBoutton(tk.Frame):
	def __init__(self, master, configs, mode, iconpath, text, hasbtn=False):
		super().__init__(master)
		self.master = master
		self.configs = configs
		self.mode = mode
		self.hasbtn = hasbtn
		self.iconpath = iconpath
		self.status="normal"

		self.config(height=70)

		self.canvas = tk.Canvas(self, width=70, height=70, highlightthickness=0)
		self.canvas.pack(side="left")

		self.label = tk.Label(self, text=text, font=("Calibri", 13))
		self.label.pack(side="left", fill="y")

		if self.hasbtn:
			self.toggle_btn = Toggle(self, configs=self.configs['normal']['btn'], mode=self.mode)
			self.toggle_btn.pack(side="right", padx=(0, 30))
			self.master.toggle_btn = self.toggle_btn

		self.bind("<Enter>", lambda *args: self.hover("hovered"))
		self.bind("<Leave>", lambda *args: self.hover("normal"))
		self.update_mode()

	def hover(self, state):
		self.status = state
		self.update_mode()

	def update_mode(self, mode=None):
		if mode: self.mode = mode

		self.load_icon()

		self.config(bg=self.configs[self.status]['.'][self.mode])
		self.canvas.config(bg=self.configs[self.status]['icon'][self.mode])
		self.label.config(bg=self.configs[self.status]['lbl']['bg'][self.mode])
		self.label.config(fg=self.configs[self.status]['lbl']['fg'][self.mode])
		if self.hasbtn: self.toggle_btn.config(bg=self.configs[self.status]['btn']['.'][self.mode])

	def load_icon(self):
		self.canvas.delete("all")
		self.icon = utils.load_image((self.mode, self.iconpath))
		self.canvas.create_image(35, 35, image=self.icon)


class Sidebar(tk.Frame):
	def __init__(self, master, configs, mode):
		super().__init__(master)
		self.configs = configs
		self.mode = mode

		self.profile_id_var = tk.StringVar(value="@backslash057")
		self.profile_nick_var = tk.StringVar(value="Backslash")


		self.width = 400
		self.pack_propagate(False)

		self.posx = -self.width
		self.add_widgets()
		self.update_mode()

	def add_widgets(self):
		# border
		self.border = tk.Frame(self, width=2)
		self.border.pack(fill="y", side="right")

		self.close = tk.Canvas(self, width=70, height=70, highlightthickness=0, cursor="hand2")
		self.close.pack(anchor="ne")
		self.close.bind("<Button-1>", lambda *args: self.hide())
		self.load_close_icon()

		self.profile_box = tk.Frame(self)
		self.profile_box.pack(fill="x")

		self.profile_image = utils.load_image("profile.png")
		self.profile = tk.Canvas(self.profile_box, width=100, height=100, highlightthickness=0)
		self.profile.pack(side="left", padx=20)
		self.profile.create_image(50, 50, image=self.profile_image)

		self.profile_labels = tk.Frame(self.profile_box, bg="#fff")
		self.profile_labels.pack(side="left", fill="both")

		nickfont = tkFont.Font(family="Calibri", size="13")
		idfont = tkFont.Font(family="Calibri", size="9")
		self.profile_nick = tk.Label(self.profile_labels, font=nickfont, textvariable=self.profile_nick_var)
		self.profile_nick.pack(anchor="w", side="bottom")
		self.profile_id = tk.Label(self.profile_labels, font=idfont, textvariable=self.profile_id_var)
		self.profile_id.pack(anchor="w", side="bottom", before=self.profile_nick)


		#separator
		self.separator = tk.Frame(self, height=3)
		self.separator.config(bg=self.configs['separator'][self.mode])
		self.separator.pack(fill="x", pady=(30, 10))
		
		self.groupes = SidebarBoutton(self, configs=self.configs['sbarbtn'], mode=self.mode, iconpath="group.png", text="New group")
		self.groupes.pack(fill="x")

		self.chat = SidebarBoutton(self, configs=self.configs['sbarbtn'], mode=self.mode, iconpath="contact.png", text="New chat")
		self.chat.pack(fill="x")

		self.favs = SidebarBoutton(self, configs=self.configs['sbarbtn'], mode=self.mode, iconpath="favorites.png", text="Saved messages")
		self.favs.pack(fill="x")

		self.toggle_set = SidebarBoutton(
									self,
									configs=self.configs['sbarbtn'],
									mode=self.mode,
									iconpath="night_mode.png",
									text="Night mode",
									hasbtn=True
								)

		self.toggle_set.pack(fill="x")

		self.infobox = tk.Frame(self)
		self.infobox.pack(side="bottom", anchor="w", padx=(40, 0), pady=(0, 20))

		namefont = tkFont.Font(family="Calibri", size=13, weight="bold")
		self.appname = tk.Label(self.infobox, text="KNova chat", font=namefont)
		self.appname.pack(anchor="w")

		namefont = tkFont.Font(family="Calibri", size=10)
		self.appversion = tk.Label(self.infobox, text=self.configs['version'], font=namefont)
		self.appversion.pack(anchor="w")


	@property
	def hidden(self):
		return self.posx==-self.width

	def place_(self):
		self.place(x=self.posx, y=0, relheight=1.0)

	def toggle(self):
		if self.posx == -self.width:
			self.reveal()
		else:
			self.hide()

	def hide(self):
		if self.posx > -self.width:
			self.posx -= 8
			self.place(x=self.posx)
			self.after(2, self.hide)
		else:
			self.posx = -self.width
		

	def reveal(self):
		if self.posx < 0:
			self.posx += 8
			self.place(x=self.posx)
			self.after(2, self.reveal)
		else:
			self.posx=0

	def update_mode(self, mode=None):
		if mode: self.mode = mode

		self.load_close_icon()

		self.config(bg=self.configs['.'][self.mode], width=self.width)
		self.border.config(bg=self.configs['border'][self.mode])
		self.close.config(bg=self.configs['close'][self.mode])
		self.profile_box.config(bg=self.configs['profilebox']['.'][self.mode])
		self.profile.config(bg=self.configs['profilebox']['profile'][self.mode])
		self.profile_labels.config(bg=self.configs['profilebox']['plabels']['.'][self.mode])
		self.profile_nick.config(bg=self.configs['profilebox']['plabels']['nick']['bg'][self.mode])
		self.profile_nick.config(fg=self.configs['profilebox']['plabels']['nick']['fg'][self.mode])
		self.profile_id.config(bg=self.configs['profilebox']['plabels']['id']['bg'][self.mode])
		self.profile_id.config(fg=self.configs['profilebox']['plabels']['id']['fg'][self.mode])
		self.separator.config(bg=self.configs['separator'][self.mode])

		self.groupes.update_mode(self.mode)
		self.chat.update_mode(self.mode)
		self.favs.update_mode(self.mode)
		self.toggle_set.update_mode(self.mode)

		self.infobox.config(bg=self.configs['infobox']['.'][self.mode])
		self.appname.config(bg=self.configs['infobox']['appname']['bg'][self.mode])
		self.appname.config(fg=self.configs['infobox']['appname']['fg'][self.mode])
		self.appversion.config(bg=self.configs['infobox']['appversion']['bg'][self.mode])
		self.appversion.config(fg=self.configs['infobox']['appversion']['fg'][self.mode])

	def load_close_icon(self):
		self.close_icon = utils.load_image((self.mode, "close.png"), (40, 40))
		self.close.create_image(35, 35, image=self.close_icon)


# fin