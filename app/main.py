from fastapi import FastAPI
from app.pipeline.processor import processor

app = FastAPI(title="Text-to-Image Multi-Model Pipeline")

@app.get("/")
def health_check():
    return {"status": "API is running"}
