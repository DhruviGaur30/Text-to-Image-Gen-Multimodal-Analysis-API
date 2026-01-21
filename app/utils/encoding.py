# app/utils/encoding.py
import base64
import io
from PIL import Image


def pil_image_to_base64(image: Image.Image) -> str:
    """
    Convert a PIL Image directly to base64 (no file saving).
    """
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)
    return base64.b64encode(buffer.read()).decode("utf-8")
