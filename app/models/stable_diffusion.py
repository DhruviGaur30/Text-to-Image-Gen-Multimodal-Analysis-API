from diffusers import StableDiffusionPipeline
import torch

class ImageGenerator:
    def __init__(self, device):
        self.device = device
        self.pipe = StableDiffusionPipeline.from_pretrained(
            "runwayml/stable-diffusion-v1-5"
        )
        self.pipe.to(self.device)

    def generate(self, prompt: str):
        result = self.pipe(prompt)
        return result.images[0]
