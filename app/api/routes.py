from fastapi import APIRouter, UploadFile, File, HTTPException
from app.pipeline.processor import processor

router = APIRouter()


@router.post("/generate")
def generate(prompt: str):
    try:
        return processor.generate(prompt)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/analyze")
def analyze(file: UploadFile = File(...)):
    try:
        return processor.analyze(file)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/health")
def health():
    return {"status": "ok"}
