from view import gui



try:
	app = gui.GUI()
	app.mainloop()
except KeyboardInterrupt:
	pass