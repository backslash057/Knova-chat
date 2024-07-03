from PIL import Image

w, h = 1418, 1039

image = Image.new("RGB", (w, h), color="white")

start = (207, 213, 140)
middle = (123, 180, 135)
end = (207, 213, 140)


for x in range(w):
    for y in range(h):
        if x + y < w:
            ratio = (x + y) / (w - 1)
            color = (
                int(start[0] + (middle[0] - start[0]) * ratio),
                int(start[1] + (middle[1] - start[1]) * ratio),
                int(start[2] + (middle[2] - start[2]) * ratio)
            )
        else:
            ratio = (x + y - w) / (h - 1)
            color = (
                int(middle[0] + (end[0] - middle[0]) * ratio),
                int(middle[1] + (end[1] - middle[1]) * ratio),
                int(middle[2] + (end[2] - middle[2]) * ratio)
            )
        image.putpixel((x, y), color)

image.save("image_final.png", "PNG")
