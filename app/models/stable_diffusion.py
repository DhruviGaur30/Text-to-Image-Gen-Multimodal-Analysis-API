import torch
from diffusers import StableDiffusionPipeline


class ImageGenerator:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        self.pipe = StableDiffusionPipeline.from_pretrained(
            "runwayml/stable-diffusion-v1-5",
            torch_dtype=torch.float32
        )

        self.pipe.to(self.device)

    def generate(self, prompt: str):
        return self.pipe(prompt).images[0]
