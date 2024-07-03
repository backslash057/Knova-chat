#builtin libraries
import tkinter as tk

# third party libraries
import yaml

# local libraries
from .sidebar import Sidebar
from .groupbar import Groupbar
from .chatmenu import Chatmenu
from .titlebar import Titlebar
from .chatzone import Chatzone
from .messagebar import Messagebar
from .utils import load_icon
from .login import Authentify

from controllers.networkcontroller import network



# activating DPI awareness to prevent blurred widgets
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

# main GUI App
class GUI(tk.Tk):
	def __init__(self):
		super().__init__()
		

	def init(self, config, mode="light"):
		self.configs = config
		self.mode = mode
		
		self.set_window()
		self.add_widgets()


	def set_window(self):
		self.minsize(1600, 800)
		self.title("Chat")
		self.iconbitmap(load_icon("chat.ico"))
		#self.protocol("WM_DELETE_WINDOW", lambda: print(self.winfo_width(), self.winfo_height()))
		self.state('zoomed')


	def add_widgets(self):
		auth_container = tk.Frame(self, bg="#fff")

		self.auth = Authentify(auth_container)
		self.auth.pack(expand=True)


		app_container = tk.Frame(self, highlightthickness=0)

		self.groupbar = Groupbar(app_container, togglebar=self.toggle_sidebar)
		self.groupbar.pack(side="left", fill="y")

		self.chatmenu = Chatmenu(app_container, self.configs['chatmenu'], self.mode)
		self.chatmenu.pack(side="left", fill="y")

		msg_zone = tk.Frame(app_container, highlightthickness=0)
		msg_zone.pack(side="left", expand=True, fill="both")

		self.titlebar = Titlebar(msg_zone, configs=self.configs['titlebar'], mode=self.mode)
		self.titlebar.pack(fill="x")

		self.chat = Chatzone(msg_zone, configs=self.configs['chatzone'], mode=self.mode)
		self.chat.pack(expand=True, fill="both")
		self.chat.bind("<<config>>", lambda: print("modifié"))

		self.msgbar = Messagebar(msg_zone, configs=self.configs['msgbar'], mode=self.mode)
		self.msgbar.pack(fill="x")
		

		self.sidebar = Sidebar(self, self.configs['sidebar'], self.mode)
		self.sidebar.toggle_btn.oncommand = self.toggle_dark
		self.sidebar.toggle_btn.offcommand = self.toggle_light

		
		#app_container.place(relheight=1.0, relwidth=1.0)
		#self.sidebar.place_()
		auth_container.pack(fill="both", expand=True)

	def toggle_dark(self):
		self.mode = "dark"
		self.chatmenu.update_mode(self.mode)
		self.sidebar.update_mode(self.mode)
		self.titlebar.update_mode(self.mode)
		self.chat.update_mode(self.mode)
		self.msgbar.update_mode(self.mode)

	def toggle_light(self):
		self.mode = "light"
		self.chatmenu.update_mode(self.mode)
		self.sidebar.update_mode(self.mode)
		self.titlebar.update_mode(self.mode)
		self.chat.update_mode(self.mode)
		self.msgbar.update_mode(self.mode)

	def toggle_sidebar(self):
		self.sidebar.toggle()

	def stop_loader(self):
		self.auth.submit.stop_loader()


gui = GUI()
