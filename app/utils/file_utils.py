from datetime import datetime
from pathlib import Path
from typing import BinaryIO

from app.core.config import OUTPUT_DIR


def save_uploaded_file(file: BinaryIO, prefix: str = "uploaded") -> str:
    """
    Saves an uploaded file to disk and returns the file path.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{prefix}_{timestamp}.png"
    path = Path(OUTPUT_DIR) / filename

    with open(path, "wb") as buffer:
        buffer.write(file.read())

    return str(path)
