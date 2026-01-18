from fastapi import APIRouter
from app.pipeline.processor import PipelineProcessor

router = APIRouter()

@router.post("/generate")
def generate(prompt: str):
    image, clip_data, segmentation = processor.run(prompt)

    return {
        "clip_analysis": clip_data,
        "basic_segmentation": segmentation
    }
