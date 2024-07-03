import tkinter as tk 


root = tk.Tk()
root.config(bg="red")
root.wm_attributes("-transparentcolor", "#fffffe") 

cnv = tk.Canvas(root, bg="#fffffe")

cnv.pack()

root.mainloop()