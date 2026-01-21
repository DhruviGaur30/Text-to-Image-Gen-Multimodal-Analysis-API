import logging
from pathlib import Path
from typing import Dict, Any

from PIL import Image

from app.models.clip_model import ClipAnalyzer
from app.models.sam_model import SamSegmenter
from app.models.stable_diffusion import ImageGenerator

from app.utils.encoding import pil_image_to_base64
from app.utils.image_utils import visualize_regions
from app.utils.file_utils import save_uploaded_file

from app.core.config import OUTPUT_DIR

logger = logging.getLogger(__name__)


class MultiModelProcessor:
    def __init__(self):
        logger.info("Initializing multimodel processor")

        self.generator = ImageGenerator()
        self.clip = ClipAnalyzer()
        self.segmenter = SamSegmenter()

        Path(OUTPUT_DIR).mkdir(exist_ok=True)

    # -------------------------
    # TEXT → IMAGE
    # -------------------------
    def generate(self, prompt: str) -> Dict[str, Any]:
        image_path = self.generator.generate(prompt)
        return {"image_path": image_path}

    # -------------------------
    # IMAGE ANALYSIS
    # -------------------------
    def analyze(self, file) -> Dict[str, Any]:
        try:
            image_path = save_uploaded_file(file.file, prefix="uploaded")
            image = Image.open(image_path).convert("RGB")

            clip_results = self.clip.analyze_image(image)
            region_results = self.clip.analyze_regions(image)
            segmentation = self.segmenter.segment(image)

            visualized_image = visualize_regions(image, region_results)
            visualization_base64 = pil_image_to_base64(visualized_image)

            return {
                "image_path": image_path,
                "clip_analysis": clip_results,
                "region_clip_analysis": region_results,
                "segmentation": segmentation,
                "visualization_base64": visualization_base64,
            }

        except Exception as e:
            logger.exception("Image analysis failed")
            raise RuntimeError(f"Analysis failed: {str(e)}")

# Singleton instance
processor = MultiModelProcessor()
