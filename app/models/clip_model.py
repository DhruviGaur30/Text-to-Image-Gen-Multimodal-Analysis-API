from transformers import CLIPProcessor, CLIPModel
import torch

class ClipAnalyzer:
    def __init__(self, device):
        self.device = device
        self.model = CLIPModel.from_pretrained(
            "openai/clip-vit-base-patch32"
        ).to(device)
        self.processor = CLIPProcessor.from_pretrained(
            "openai/clip-vit-base-patch32"
        )

    def analyze(self, image, concepts):
        inputs = self.processor(
            text=concepts,
            images=image,
            return_tensors="pt",
            padding=True
        ).to(self.device)

        outputs = self.model(**inputs)
        probs = outputs.logits_per_image.softmax(dim=1)[0]

        return dict(zip(concepts, probs.tolist()))
