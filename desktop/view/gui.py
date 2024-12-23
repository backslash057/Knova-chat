import customtkinter as ctk
import tkinter as tk


from .login import login

import sys
if sys.platform == 'win32':
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)


class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        
        auth_page = tk.Frame(self)

        auth_page.place(0, 0, relwidth=1.0, relheight=1.0)


gui = Gui()