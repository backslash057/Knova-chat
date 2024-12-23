import tkinter as tk 
import customtkinter as ctk

class AuthPageBase(tk.Frame):
	def __init__(self, master):
		super().__init__(master)
		self.config(bg="red")

		# TEMPORARY => for unitary auth widgets testing
		self.pack_configure(expand=True, fill="both")

		self.form = tk.CtkFrame(self,
			width = 100,
			height = 100,
			bg_color=

		)
		self.form.pack()





class LoginPage(AuthPageBase):
	def __init__(self, master):
		super().__init__(master)

	def submit(self):
		pass

class SignupPage(AuthPageBase):
	def __init__(self, master):
		super().__init__(master)


	def submit(self):
		pass

class QRCheckPage(tk.Frame):
	def __init__(self, master):
		super().__init__(master)
