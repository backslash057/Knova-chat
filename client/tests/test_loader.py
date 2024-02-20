import tkinter as tk
import os
from PIL import Image, ImageTk

class Loader(tk.Canvas):
    def __init__(self, master, path, width=64, height=64, bg="#ffffff"):
        super().__init__(master, width=width, height=height, bg=bg, highlightthickness=0)

        self.images = self.load_images(path)  # Charger et conserver les images dans self.images
        self.image_refs = []  # Liste pour conserver les références aux images

        for img in self.images:
            img_ref = ImageTk.PhotoImage(img)
            self.image_refs.append(img_ref)  # Conserver les références aux images

        self.frame_index = 0
        self.running = False
        self.start()

    def load_images(self, path):
        images = []
        files = sorted(os.listdir(path))
        print(files)

        for file in files:
            image = Image.open(os.path.join(path, file))
            images.append(image)
        return images

    def start(self):
        self.running = True
        self.animate()

    def animate(self):
        if self.running:
            self.delete("all")
            self.create_image(32, 32, image=self.image_refs[self.frame_index])
            self.frame_index = (self.frame_index + 1) % len(self.image_refs)
            self.after(45, self.animate)

    def stop(self):
        self.running = False
        self.frame_index = 0

root = tk.Tk()
root.geometry("400x400")

loader = Loader(root, path="loader")
loader.pack()
root.mainloop()
