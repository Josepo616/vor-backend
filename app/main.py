from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

@app.get("/")
async def root():
    return {"message": "Vor API is running correctly,", "status": "OK"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}