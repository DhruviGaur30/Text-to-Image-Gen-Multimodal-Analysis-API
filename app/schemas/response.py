from pydantic import BaseModel
from typing import Dict, List

class ClipAnalysis(BaseModel):
    concepts: Dict[str, float]

class Segmentation(BaseModel):
    masks: List
    polygons: List
