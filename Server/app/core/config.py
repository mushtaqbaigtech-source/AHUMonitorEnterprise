from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "AHUMonitor Enterprise"
    APP_VERSION: str = "1.0.0"

    HOST: str = "0.0.0.0"
    PORT: int = 8000

    SECRET_KEY: str

    DATABASE_URL: str

    SCREENSHOT_PATH: str = "storage/screenshots"
    METADATA_PATH: str = "storage/metadata"
    LOG_PATH: str = "logs"

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True
    )


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()