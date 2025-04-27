# config.py

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    BACKEND_HOST: str = "http://127.0.0.1"
    BACKEND_PORT: int = 8000

    CLIENT_HOST: str = "http://127.0.0.1"
    CLIENT_PORT: int = 3000

    class Config:
        env_file = ".env"  # optional, loads from .env if available

settings = Settings()
