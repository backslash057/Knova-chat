import tkinter as tk 


from controllers.network import network

class TestGUI(tk.Tk):
	def __init__(self):
		super().__init__()
		self.geometry("300x200")
		self.entry_var = tk.StringVar()

		entry = tk.Entry(self, textvariable=self.entry_var)
		entry.pack(expand=True)

		btn = tk.Button(self, text="Send", command=lambda: network.send_datas(self.entry_var.get()))
		btn.pack(expand=True)
