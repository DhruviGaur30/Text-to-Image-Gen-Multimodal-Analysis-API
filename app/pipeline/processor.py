import torch
from app.models.stable_diffusion import ImageGenerator
from app.models.clip_model import ClipAnalyzer
from app.models.sam_model import SamSegmenter

device = "cuda" if torch.cuda.is_available() else "cpu"

image_generator = ImageGenerator(device)
clip_analyzer = ClipAnalyzer(device)
sam_segmenter = SamSegmenter()

class PipelineProcessor:
    def run(self, prompt: str):
        image = image_generator.generate(prompt)
        clip_result = clip_analyzer.analyze(
            image,
            ["cat", "dog", "person", "car", "tree"]
        )
        segmentation = sam_segmenter.segment(image)

        return {
            "clip_analysis": clip_result,
            "basic_segmentation": segmentation
        }

processor = PipelineProcessor()
