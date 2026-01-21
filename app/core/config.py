import torch
from pathlib import Path

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# Output paths
BASE_DIR = Path(__file__).resolve().parent.parent.parent
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

# CLIP labels
DEFAULT_LABELS = [
    "person",
    "human",
    "face",
    "hat",
    "glasses",
    "clothing",
    "animal",
    "object",
    "background",
    "sky",
    "building",
    "tree",
    "water",
    "food",
    "fruit",
]
