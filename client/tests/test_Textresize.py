import tkinter as tk 

from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

root = tk.Tk()
root.geometry("500x500+700+200")
root.config(bg="green")

container = tk.Frame(root, height=70, highlightthickness=0)
container.pack(side="bottom", fill="x")

text = tk.Text(container, bg="red", height=1)
text.pack(side="bottom", fill="x")

text.bind("<KEYDOW>", lambda: print("changement..."))

root.winfo_x
root.mainloop()