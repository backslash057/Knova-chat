import tkinter as tk 
from tkinter import font as tkFont


root = tk.Tk()

lbl = tk.Label(root ,text="i", font = tkFont.Font(family="Calibri", size=20))


print(lbl.winfo_reqwidth())