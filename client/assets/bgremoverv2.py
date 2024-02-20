from PIL import Image

image = Image.open("knova-light.png")
image = image.convert("RGBA")

data = image.getdata()

new_data = []
for item in data:
    if item == (255, 255, 255, 255):
        item = (*item[:-1], 0)
    new_data.append(item)

image.putdata(new_data)
image.save("knova-savetr.png", "PNG")  




