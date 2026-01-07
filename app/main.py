from fastapi import FastAPI
from app.core.config import settings
from app.models.user import User
from app.models.job import JobReq
from app.models.candidate import Candidate 
from app.api.v1.api import api_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# CORS settings - Allow all origins for development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, specify allowed origins (e.g., your frontend URL)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
async def root():
    return {"message": "Vor API is running correctly,", "status": "OK"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
