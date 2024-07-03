import os 
import os.path

from PIL import Image, ImageTk

assets_path = "assets/"

def load_images(path):
	images = []

	path = os.path.join(assets_path, path)

	for file in os.listdir(path):
		image = Image.open(os.path.join(path, file))
		images.append(image)

	return images


def load_image(file, scale=None):
	if type(file) == str:
		path = os.path.join(assets_path, file)
	elif type(file) == tuple:
		path = os.path.join(assets_path, *file)
	else:
		raise Exception(f"Le type \"{type(file)}\" n'est pas supporté")

	image = Image.open(path)
	if scale: image = image.resize(scale)

	return ImageTk.PhotoImage(image)

def load_icon(file):
	path = os.path.join(assets_path, file)
	if not os.path.exists(path):
		raise Exception(f"Erreur de chargement de l'icone au chemin \"{path}\"")
	return 

