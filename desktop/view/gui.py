import customtkinter as ctk
import tkinter as tk

from . import auth


# amelioratiing process DPI for Windows
import sys
if sys.platform == 'win32':
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)


class GUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.set_window()
        
        login_page = auth.LoginPage(self)

        login_page.pack()

    def set_window(self):
        self.minsize(500, 500)
