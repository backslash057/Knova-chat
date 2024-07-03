from PIL import Image, ImageDraw
w, h = 3840, 2160
def generate_gradient(background_color, circles):
    

    image = Image.new("RGB", (w, h), color=background_color)

    draw = ImageDraw.Draw(image)

    for circle in circles:
        position, radius, color = circle
        center_x, center_y = position

        for x in range(w):
            for y in range(h):
                distance = ((x - center_x) ** 2 + (y - center_y) ** 2) ** 0.5
                
                if distance <= radius:
                    ratio = distance / radius
                    gradient_color = (
                        int(color[0] + (background_color[0] - color[0]) * ratio),
                        int(color[1] + (background_color[1] - color[1]) * ratio),
                        int(color[2] + (background_color[2] - color[2]) * ratio)
                    )
                    draw.point((x, y), fill=gradient_color)

    image.save("image_final.png", "PNG")

# Exemple d'utilisation de la fonction
background_color = (123, 180, 135)  # Couleur d'arrière-plan (blanc)
circles = [((0, 0), h-100, (207, 213, 140)), ((w, h), 300, (207, 213, 140))]  # Liste de cercles (position, rayon, couleur)

generate_gradient(background_color, circles)
