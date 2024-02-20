# builtin libraries
import tkinter as tk 
import customtkinter as ctk
from tkinter import font as tkFont

# local libraries
from controllers import networkcontroller
from controllers import authcontroller

from . import utils


# third party libraries
import os
import os.path
from PIL import Image, ImageTk


class Authentify(tk.Frame):
	def __init__(self, master, *args, **kwargs):
		super().__init__(master, *args, **kwargs)
		self.config(bg="#fff")

		self.add_widgets()

	def add_widgets(self):
		w, h = 130, 130
		logo_icon = utils.load_image("knova-logo.png", (w, h))
		self.logo = tk.Canvas(self, width=w, height=h, bg="#ffffff", highlightthickness=0)
		self.logo.image = logo_icon
		self.logo.pack(expand=True)
		self.logo.create_image(w//2, h//2, image=logo_icon)
		
		self.errorbox = Errorframe(self, self.logo)
		#self.errorbox.pack(fill="x", after=self.logo, pady=(15, 0))

		self.main = ctk.CTkFrame(self, fg_color="#F6F8FA", bg_color="#ffffff")
		self.main.configure(border_color="#D8DEE4", border_width=1)
		self.main.pack(pady=(20, 0), fill="x", expand=True)

		font=("Calibri", 12)
		self.username = KInput(self.main, text="User id", textfont=font)
		self.username.pack(anchor="w", fill="x", padx=30, pady=(22, 0))

		self.nickname = KInput(self.main, text="Nickname", textfont=font)
		self.nickname.pack(anchor="w", fill="x", padx=30, pady=(22, 0))

		self.password = KInput(self.main, text="Password", textfont=font, show="•")
		self.password.pack(anchor="w", fill="x", padx=30, pady=(22, 0))


		validation = tk.Frame(self.main, bg="#F6F8FA")
		validation.pack(fill="x", pady=20, padx=30)

		targets = [self.username, self.nickname, self.password]
		self.submit = KSubmit(validation, handler=self.error_handler, targets=targets, errorbox=self.errorbox)
		self.submit.pack(side="right")

		font = tkFont.Font(family="Calibry", size=10, underline=True)
		self.auth_mode = tk.Label(validation, text="Log in", font=font, bg="#F6F8FA", fg="#46A2D9", cursor="hand2")
		self.auth_mode.pack(side="right", padx=(0, 6), anchor="s")
		self.auth_mode.bind("<Button-1>", lambda *args: self.set_login())

		self.mode_label = tk.Label(validation, text="Already registered? ", font=("Calibri", 9), bg="#F6F8FA", fg="#888888")
		self.mode_label.pack(side="right", anchor="s")

	def set_login(self):
		if self.submit.loader.running: return

		self.errorbox.pack_forget()

		self.username.clear()
		self.nickname.clear()
		self.nickname.pack_forget()
		self.password.clear()
		self.auth_mode.config(text="Register")
		self.mode_label.config(text="No account? ")
		self.submit.label.config(text="Login")
		self.auth_mode.bind("<Button-1>", lambda *args: self.set_register())

	def set_register(self):
		if self.submit.loader.running: return

		self.errorbox.pack_forget()

		self.username.clear()
		self.nickname.clear()
		self.nickname.pack(anchor="w", after=self.username, fill="x", padx=30, pady=(22, 0))
		self.password.clear()
		self.auth_mode.config(text="Log in")
		self.mode_label.config(text="Already registered? ")
		self.submit.label.config(text="Register")
		self.auth_mode.bind("<Button-1>", lambda *args: self.set_login())

	def error_handler(self, error):
		self.errorbox.pack(fill="x", after=self.logo, pady=(15, 0))


class KSubmit(ctk.CTkFrame):
	def __init__(self, master, handler, targets, errorbox, command=None):
		super().__init__(master, cursor="hand2")

		self.errorbox = errorbox

		self.normal_color = "#3CB6B6"
		self.blocked_color = "#148e8e"
		self.status = "normal"
		self.targets = targets

		self.handler = handler

		self.container = tk.Frame(self)
		self.container.pack(fill="both", padx=25, pady=8)

		self.label = tk.Label(self.container, text="Register", font=("Calibri", 14), fg="#ffffff")
		self.label.pack(side="left", expand=True)

		self.loader = Loader(self.container, path="loader", width=40, height=40)

		self.bind("<Button-1>", lambda *args: self.start_loader())
		self.container.bind("<Button-1>", lambda *args: self.start_loader())
		self.label.bind("<Button-1>", lambda *args: self.start_loader())

		self.update_color()
	
	def start_loader(self):
		for target in self.targets:
			target.disable()

		self.container.unbind("<Button-1>")
		self.label.unbind("<Button-1>")

		self.loader.pack(side="left", padx=(5, 0), expand=True)
		self.loader.start()
		

		def deactivate():
			if self.loader.running:
				self.stop_loader()
				self.errorbox.display("Network Error. Try later")


		self.after(8000, deactivate)
		self.errorbox.pack_forget()
		self.update_color("blocked")

		self.validate_entries()

	def stop_loader(self):
		for target in self.targets:
			target.enable()

		self.bind("<Button-1>", lambda *args: self.start_loader())
		self.container.bind("<Button-1>", lambda *args: self.start_loader())
		self.label.bind("<Button-1>", lambda *args: self.start_loader())

		self.loader.pack_forget()
		self.loader.stop()
		self.update_color("normal")
	
	def update_color(self, state=None):
		if state: self.status = state 

		color = self.normal_color if self.status=="normal" else self.blocked_color

		self.configure(fg_color=color)
		self.container.config(bg=color)
		self.label.configure(bg=color)
		self.loader.configure(bg=color)


	def validate_entries(self):
		username = self.targets[0].entry.text.get()
		callback = authcontroller.validate_username(username)
		if callback:
			def stop():
				self.stop_loader()
				self.errorbox.display(callback)
			self.after(100, stop)
			return

		nickname = self.targets[1].entry.text.get()
		if self.targets[1].entry.entry.winfo_viewable():
			callback = authcontroller.validate_nickname(nickname)
			if callback:
				def stop():
					self.stop_loader()
					self.errorbox.display(callback)
				self.after(100, stop)
				return

		password = self.targets[2].entry.text.get()
		callback = authcontroller.validate_password(password)
		if callback:
			def stop():
				self.stop_loader()
				self.errorbox.display(callback)
			self.after(200, stop)
			return


		if not self.targets[1].entry.entry.winfo_viewable(): nickname=None

		try:
			networkcontroller.send_auth_datas(username, nickname, password)
		except OSError as e:
			print(e)



class KInput(tk.Frame):
	def __init__(self, master, text, textfont, show=None):
		super().__init__(master, bg=master.cget("fg_color"))

		label = tk.Label(self, text=text, fg="#888888", bg="#F6F8FA", font=textfont)
		label.pack(anchor="w")

		self.entry = KEntry(self, show=show)
		self.entry.pack(anchor="w", fill="x", pady=(5, 0))

	def clear(self):
		self.entry.clear()

	def enable(self):
		self.entry.entry.config(state="normal")

	def disable(self):
		self.entry.entry.config(state="readonly")

class KEntry(ctk.CTkFrame):
	def __init__(self, master, show=None):
		super().__init__(master, width=280, height=35, fg_color="#ffffff", border_color="#D0D7DE", border_width=1)
		self.pack_propagate(False)
		self.text = tk.StringVar()

		font=tkFont.Font(family="Calibri", size=12)
		self.entry = tk.Entry(self, relief="flat", fg="#1F2328", readonlybackground="#ffffff", font=font)
		self.entry.config(textvariable=self.text)
		self.entry.pack(fill="x", expand=True, padx=10)
		if show: self.entry.config(show=show)

		self.bind("<Button-1>", lambda *args: self.entry.focus_set())
		self.entry.bind("<FocusIn>", lambda *args: self.set_active())
		self.entry.bind("<FocusOut>", lambda *args: self.set_normal())

	def clear(self):
		self.entry.delete("0", "end")

	def set_active(self):
		self.configure(border_color="#0969DA", border_width=1)

	def set_normal(self):
		self.configure(border_color="#D0D7DE", border_width=1)



class Errorframe(ctk.CTkFrame):
	def __init__(self, master, before):
		super().__init__(master)
		self.before = before
		self.configure(height=40, fg_color="#FFEBE9", bg_color="#ffffff", border_color="#FFC1C0", border_width=1)

		font = tkFont.Font(family="Calibri", size=14)
		self.text = tk.Label(self, text="Message", bg="#FFEBE9", font=font)
		self.text.config(fg="#6F2328")
		self.text.pack(side="left", padx=20)
		self.icon = tk.Canvas(self, bg="#FFEBE9", highlightthickness=0, width=40, height=40, cursor="hand2")
		self.icon.pack(side="right", pady=12, padx=15)
		self.icon_res = utils.load_image("close-error.png")
		self.icon.create_image(20, 20, image=self.icon_res)

		self.icon.bind("<Button-1>", lambda *args: self.pack_forget())

	def display(self, message):
		self.text.config(text=message)

		self.pack(fill="x", pady=(15, 0), after=self.before)


	def hide(self):
		self.pack_forget()

class Loader(tk.Canvas):
    def __init__(self, master, path, width=40, height=40, bg="#ffffff"):
        super().__init__(master, width=width, height=height, bg=bg, highlightthickness=0)

        self.images = []
        self.load_images(path)

        self.frame_index = 0
        self.running = False

    def load_images(self, path):
        imgs = utils.load_images("loader")

        for img in imgs:
            image = ImageTk.PhotoImage(img)
            self.images.append(image)

    def start(self):
        self.running = True
        self.animate()

    def animate(self):
        if self.running:
            self.delete("all")
            self.create_image(20, 20, image=self.images[self.frame_index])
            self.frame_index = (self.frame_index + 1) % len(self.images)
            self.after(45, self.animate)

    def stop(self):
        self.running = False
        self.frame_index = 0