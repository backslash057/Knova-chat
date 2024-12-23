# builtin libraries
import tkinter as tk 
import customtkinter as ctk
from tkinter import font as tkFont

# local libraries
from controllers import networkcontroller
from controllers import authcontroller

from . import utils
from .login_widgets import KInputbox, KEntry, KSubmit, Errorframe


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
		
		self.errorbox = Errorframe(self)
		#self.errorbox.pack(fill="x", after=self.logo, pady=(15, 0))

		self.main = ctk.CTkFrame(self, fg_color="#F6F8FA", bg_color="#ffffff")
		self.main.configure(border_color="#D8DEE4", border_width=1)
		self.main.pack(pady=(20, 0), fill="x", expand=True)


		self.userid_entry = KInputbox(self.main, text="User id")
		self.userid_entry.pack(anchor="w", fill="x", padx=30, pady=(22, 0))

		self.username_entry = KInputbox(self.main, text="Nickname")
		self.username_entry.pack(anchor="w", fill="x", padx=30, pady=(22, 0))

		self.password_entry = KInputbox(self.main, text="Password", show="•")
		self.password_entry.pack(anchor="w", fill="x", padx=30, pady=(22, 0))


		validation_row = tk.Frame(self.main, bg="#F6F8FA")
		validation_row.pack(fill="x", pady=20, padx=30)

		self.auth_mode_label = tk.Label(validation_row, text="Already registered? ", bg="#F6F7F8")
		self.auth_mode_label.pack(side="right", anchor="s")

		font = tkFont.Font(family="Calibri", size=10, underline=True)
		self.auth_mode_link = tk.Label(validation_row, text="Log in", font=font, bg="#F6F8FA", fg="#46A2D9", cursor="hand2")
		self.auth_mode_link.pack(side="right", padx=(0, 6), anchor="s", before=self.auth_mode_label)
		self.auth_mode_link.bind("<Button-1>", lambda *args: self.set_login())

		self.submit_btn = KSubmit(validation_row)
		self.submit_btn.pack(side="right", before=self.auth_mode_link)

		self.submit_btn.bind("<Button-1>", lambda *args: self.send_auth_request())
		self.submit_btn.container.bind("<Button-1>", lambda *args: self.send_auth_request())
		self.submit_btn.label.bind("<Button-1>", lambda *args: self.send_auth_request())

	
	def send_auth_request(self):
		def stop():
			self.stop_loader()
			self.errorbox.display(callback)

		self.submit_btn.start_loader()

		userid = userid_entry.entry.text.get()
		username = username_entry.entry.text.get()
		password = password_entry.entry.text.get()

		callback = auth_controller.validate(userid, username, password)
		
		if callback:
			self.after(100, stop)
			return

		print("Envoi de", userid, username, password)

	
	
	def set_login(self):
		if self.submit_btn.loader.running: return

		self.errorbox.pack_forget()

		self.userid_entry.clear()
		self.username_entry.clear()
		self.username_entry.pack_forget()
		self.password_entry.clear()

		self.auth_mode_label.config(text="No account? ")
		self.auth_mode_link.config(text="Register")

		self.submit_btn.label.config(text="Login")

		self.auth_mode_link.unbind("<Button-1>")
		self.auth_mode_link.bind("<Button-1>", lambda *args: self.set_register())

	def set_register(self):
		if self.submit_btn.loader.running: return

		self.errorbox.pack_forget()

		self.userid_entry.clear()
		self.username_entry.clear()
		self.username_entry.pack(anchor="w", after=self.userid_entry, fill="x", padx=30, pady=(22, 0))
		self.password_entry.clear()
		self.auth_mode_label.config(text="Already registered? ")
		self.auth_mode_link.config(text="Log in")

		self.submit_btn.label.config(text="Register")

		self.auth_mode_link.unbind("<Button-1>")
		self.auth_mode_link.bind("<Button-1>", lambda *args: self.set_login())

	def display_error(self, error):
		self.errorbox.display(error)
		self.errorbox.pack(fill="x", after=self.logo, pady=(15, 0))


