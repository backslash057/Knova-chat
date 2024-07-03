import tkinter as tk 


class Sidebar(tk.Frame):
	def __init__(self, master, *args, **kwargs):
		super().__init__(master, *args, **kwargs)

		self.place(x=-100, y=0, relheight=1.0)


root = tk.Tk()
root.config(bg="#d3d3d3")
root.geometry("300x300")

sidebar = Sidebar(root, width=100, height=100)


root.mainloop()