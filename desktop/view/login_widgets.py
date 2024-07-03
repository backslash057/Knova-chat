import tkinter as tk
import  tkinter.font  as tkFont
import customtkinter as ctk

from . import utils

from PIL import ImageTk

class KSubmit(ctk.CTkFrame):
	def __init__(self, master):
		super().__init__(master, cursor="hand2")

		self.normal_color = "#3CB6B6"
		self.blocked_color = "#148e8e"
		self.status = "normal"

		self.container = tk.Frame(self)
		self.container.pack(fill="both", padx=25, pady=8)

		self.label = tk.Label(self.container, text="Register", font=("Calibri", 14), fg="#ffffff")
		self.label.pack(side="left", expand=True)

		self.loader = Loader(self.container, path="loader", width=40, height=40)

		self.update_color()

		
	def update_color(self, state=None):
		if state: self.status = state 

		color = self.normal_color if self.status=="normal" else self.blocked_color

		self.configure(fg_color=color)
		self.container.config(bg=color)
		self.label.configure(bg=color)
		self.loader.configure(bg=color)


	def start_loader(self):
		self.loader.pack(side="left", padx=(5, 0), expand=True)
		self.loader.start()
		

		self.update_color("blocked")

	def stop_loader(self):
		self.loader.pack_forget()
		self.loader.stop()

		self.update_color("normal")



class KInputbox(tk.Frame):
	def __init__(self, master, text, show=None):
		super().__init__(master, bg=master.cget("fg_color"))

		label = tk.Label(self, text=text, fg="#888888", bg="#F6F8FA", font=("Calibri", 12))
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
	def __init__(self, master):
		super().__init__(master)
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

	def display(self, error):
		self.text.config(text=error)


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