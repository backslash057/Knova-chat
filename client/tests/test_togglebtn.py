import tkinter as tk 

from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

root = tk.Tk()
root.geometry("300x300+500+100")


class Toggle(tk.Canvas):
	def __init__(self, master, oncommand, offcommand):
		super().__init__(master)
		self.config(width=60, height=38, highlightthickness=0, bg="#fff")
		self.oncommand = oncommand
		self.offcommand = offcommand

		self.value = "off"
		self.initial = (4, 2, 30, 28)
		self.final = (29, 2, 55, 28)

		self.arc_left = self.create_arc((4, 4, 26, 26), fill="#8A8A8A", start=90, extent=180, outline="")
		self.rect = self.create_rectangle((15, 4, 40, 27), outline="", fill="#8A8A8A")
		self.arc_right = self.create_arc((29, 4, 51, 26), fill="#8A8A8A", start=-90, extent=180, outline="")

		self.ball = self.create_oval(self.initial, fill="#fff", outline="#8A8A8A", width=4)

		self.bind("<Button-1>", self.toggle)

	def toggle(self, event):
		self.unbind("<Button-1>")
		if self.value == "off":
			self.right()
			self.value = "on"
		elif self.value == "on":
			self.left()
			self.value = "off"

	def right(self):
		pos = self.coords(self.ball)
		if pos[0] < self.final[0]:
			dest = (min(pos[0]+6, self.final[0]), pos[1], min(pos[2]+6, self.final[2]), pos[3])
			self.coords(self.ball, dest)
			self.after(20, self.right)
		else:
			self.coords(self.ball, self.final)
			self.recolor()
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
			self.recolor()
			self.bind("<Button-1>", self.toggle)
			if self.offcommand: self.offcommand()

	def recolor(self):
		if self.value == "on":
			self.itemconfig(self.ball, outline="#5288C1", fill="#17212B")
			self.itemconfig(self.arc_left, fill="#5288C1")
			self.itemconfig(self.rect, fill="#5288C1")
			self.itemconfig(self.arc_right, fill="#5288C1")
		else:
			self.itemconfig(self.ball, outline="#8A8A8A", fill="#ffffff")
			self.itemconfig(self.arc_left, fill="#8A8A8A")
			self.itemconfig(self.rect, fill="#8A8A8A")
			self.itemconfig(self.arc_right, fill="#8A8A8A")





toggle = Toggle(root, None, None)
toggle.pack(expand=True)
       
root.mainloop()