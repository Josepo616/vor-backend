from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Vor API"
    API_V1_STR: str = "/api/v1"

    # Auth settings
    SECRET_KEY: str = "ff209a2d9ff29c10077dd5b3ae6508a146ac369820a380368ad21e8ee8a1ff51"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30 # 30 minutes of token validity

    #Default configurations to work with docker containers
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@db:5432/vor_db"

    class Config:
        case_sensitive = True

settings = Settings()
