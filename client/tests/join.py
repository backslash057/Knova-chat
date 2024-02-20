from PIL import Image 

bg = Image.open('image_final.png')

pattern = Image.open('output-final.png')
assert bg.size == pattern.size

w, h = bg.size

bg_data = bg.getdata()
pattern_data = pattern.getdata()

final = []
for i in range(h):
	for j in range(w):
		if pattern_data[i*w+j][3] != 0:
			final.append(tuple(pattern_data[i*w+j][:-1]))
		else:
			final.append(bg_data[i*w+j])

image = Image.new("RGB", (w, h), color="white")
image.putdata(final)
image.save("mon_image_final_sans_conflit_de_nom.png", "PNG")
