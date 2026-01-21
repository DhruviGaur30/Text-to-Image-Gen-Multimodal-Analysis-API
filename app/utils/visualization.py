from PIL import ImageDraw

def draw_grid(image, grid_size=2):
    draw = ImageDraw.Draw(image)
    w, h = image.size

    for i in range(1, grid_size):
        draw.line((0, h * i // grid_size, w, h * i // grid_size), fill="red", width=2)
        draw.line((w * i // grid_size, 0, w * i // grid_size, h), fill="red", width=2)

    return image
