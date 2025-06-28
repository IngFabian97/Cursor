# Application configuration
# Settings and environment variables 

from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Configuración del proyecto
    PROJECT_NAME: str = "Platziflix"
    VERSION: str = "0.1.0"
    
    # Configuración de base de datos
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/platziflix"
    
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()

@lru_cache
def get_settings():
    return settings 