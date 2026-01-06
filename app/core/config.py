from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Vor API"
    API_V1_STR: str = "/api/v1"

    #Default configurations to work with docker containers
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@db:5432/vor_db"

    class Config:
        case_sensitive = True

settings = Settings()
