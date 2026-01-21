
from PIL import Image, ImageDraw


def visualize_regions(image: Image.Image, regions: list) -> Image.Image:
    img = image.copy()
    draw = ImageDraw.Draw(img)

    for region in regions:
        region_id = region.get("region_id")
        # No bounding boxes yet → just label regions
        draw.text(
            (10, 10 + 20 * region_id),
            f"Region {region_id}",
            fill="red"
        )

    return img
