from utils.config import load_config

from view.gui import gui

from controllers.networkcontroller import network


import threading

try:
	netconf = load_config("network.yml")
except Exception:
	print(f"configuration \"network.yml\" invalide.")


try:
	guiconf =  load_config("config.yml")
except Exception:
	print(f"configuration \"config.yml\" invalide.")


network.init(netconf)

network_thread = threading.Thread(target=network.connect, daemon=True)
network_thread.start()

gui.init(guiconf)

try:
	gui.mainloop()
except KeyboardInterrupt:
	pass