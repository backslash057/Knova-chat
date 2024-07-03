import tkinter as tk

from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

class Roundedframe(tk.Canvas):
    def __init__(self, master, corner_radius=0, border_color="black", border_width=1, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.config(bg="red")
        r = corner_radius
        w = kwargs['width']
        h = kwargs['height']
        bg = kwargs['bg']

        bc = border_color
        bw = border_width

        up_left = self.create_arc((bw, bw, r*2+bw, r*2+bw), start=90, fill=bg, outline=bc, width=bw)
        up_right = self.create_arc((w-bw-r*2, bw, w-bw, r*2), start=0, fill=bg, outline=bc, width=bw)
        down_left = self.create_arc((bw, h-bw-r*2, bw+r*2, h-bw), start=180, fill=bg, outline=bc, width=bw)
        down_right = self.create_arc((w-bw-r*2, h-bw-r*2, w-bw, h-bw), start=270, fill=bg, outline=bc, width=bw)
        rect1 = self.create_rectangle((bw+r, bw, 400, 400), fill=bg, outline="")

# Exemple d'utilisation
root = tk.Tk()
root.geometry("300x200")
root.state("zoomed")

rounded_frame = Roundedframe(root, corner_radius=100, width=1000, height=1000, bg="white", border_color="blue", border_width=10)
rounded_frame.pack(expand=True)

root.mainloop()