from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

class CommonSettings(BaseSettings):
    DEBUG_MODE: bool = bool(os.getenv('DEBUG_MODE', True))

class ServerSettings(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 8000

class DatabaseSettings(BaseSettings):
    DB_NAME: str = os.getenv('DB_NAME')
    DB_URL: str = os.getenv('DB_URL')
    
class Settings(CommonSettings, ServerSettings, DatabaseSettings):
    pass

settings = Settings()