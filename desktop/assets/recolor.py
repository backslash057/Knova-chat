import os
import os.path
from PIL import Image



files = os.listdir("loader")


for file in files:
	image = Image.open(os.path.join("loader", file)).resize((40, 40))

	data = image.getdata()
	new_data = []

	for item in data:
		if not item[3] == 0:
			item = (255, 255, 255, 255)
		new_data.append(item)

	image.putdata(new_data)
	image.save(os.path.join("loader3", file), "PNG")