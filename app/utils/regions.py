from PIL import Image

def split_into_regions(image: Image.Image, grid_size=2):
    """
    Split image into grid regions.
    grid_size=2 → 2x2 = 4 regions
    """
    w, h = image.size
    regions = []
    region_w, region_h = w // grid_size, h // grid_size

    for i in range(grid_size):
        for j in range(grid_size):
            left = j * region_w
            top = i * region_h
            right = left + region_w
            bottom = top + region_h
            regions.append(image.crop((left, top, right, bottom)))

    return regions
