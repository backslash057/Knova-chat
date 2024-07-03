import tkinter as tk 

root = tk.Tk()


cnv = tk.Canvas(root, bg="yellow")
cnv.pack()

fram = tk.Frame(cnv, bg="green", width=200, height=200)
fram.pack(side="left")

cnv.create_rectangle((10, 10, 100, 100), fill="red", outline="", tags="audessus")
cnv.pack_propagate(False)
#cnv.tag_raise("audessus")
root.mainloop()