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
    APP_NAME: str = os.getenv('APP_NAME', 'ClusterEstudo')
    DB_NAME: str = os.getenv('DB_NAME')
    DB_URL: str = f"mongodb+srv://{os.getenv('USER')}:{os.getenv('PASSWORD')}@clusterestudo.nbtnt.mongodb.net/?retryWrites=true&w=majority&appName={APP_NAME}"
    
class Settings(CommonSettings, ServerSettings, DatabaseSettings):
    pass

settings = Settings()