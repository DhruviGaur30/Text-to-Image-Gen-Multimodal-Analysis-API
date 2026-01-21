import torch
from PIL import Image
from transformers import CLIPProcessor, CLIPModel

from app.core.config import DEFAULT_LABELS
from app.utils.regions import split_into_regions


class ClipAnalyzer:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        self.model = CLIPModel.from_pretrained(
            "openai/clip-vit-base-patch32"
        ).to(self.device)

        self.processor = CLIPProcessor.from_pretrained(
            "openai/clip-vit-base-patch32"
        )

    def analyze_image(self, image: Image.Image) -> dict:
        inputs = self.processor(
            text=DEFAULT_LABELS,
            images=image,
            return_tensors="pt",
            padding=True
        ).to(self.device)

        with torch.no_grad():
            outputs = self.model(**inputs)
            probs = outputs.logits_per_image.softmax(dim=1)[0]

        return {
            label: float(prob)
            for label, prob in zip(DEFAULT_LABELS, probs)
        }

    def analyze_regions(self, image: Image.Image, grid_size: int = 2) -> list:
        regions = split_into_regions(image, grid_size)
        results = []

        for idx, region in enumerate(regions):
            scores = self.analyze_image(region)
            results.append({
                "region_id": idx,
                "scores": scores
            })

        return results
