from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    api_name: str = "SSL Checker API"
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    api_version: str = "1"

settings = Settings()