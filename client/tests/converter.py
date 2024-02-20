from PIL import Image

image = Image.open("wallpaper.jpg")

w, h = image.size
image = image.convert("RGBA")
datas = image.getdata()

new_data = []

total_pixels = w * h
pixels_processed = 0
length=60

for i in range(w):
    for j in range(h):
        item = datas[i * h + j]

        if item[0] < 87 and item[1] < 87 and item[2] < 87:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)

        pixels_processed += 1
        pct = int((pixels_processed / total_pixels) * 100)

        progress = int(pct/100 * length)
        bar = "[" + "█" * progress + " " * (length - progress) + "]" #█
        print("\r" + bar + " " + str(pct) + "%", end="")

image.putdata(new_data)
print("\nTreminé !")

image.save("output.png", "PNG")
