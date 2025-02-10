from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class Settings(BaseSettings):
    api_name: str = os.getenv("API_NAME", "SSL Checker API")
    api_host: str = os.getenv("API_HOST", "127.0.0.1")
    api_port: int = int(os.getenv("API_PORT", 8000))
    api_version: str = os.getenv("API_VERSION", "v1")

settings = Settings()