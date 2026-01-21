from fastapi import FastAPI
from app.api.routes import router
from app.core.logger import logger

app = FastAPI(
    title="Text-to-Image Multi-Model Pipeline",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def health_check():
    return {"status": "ok"}

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    logger.error(f"Unhandled error: {exc}")
    return {
        "error": "Internal Server Error"
    }
