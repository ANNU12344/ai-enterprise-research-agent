from pydantic_settings import BaseSettings, SettingsConfigDict

from app.config import Settings
class Settings(BaseSettings):
    app_name: str = "AI Enterprise Research & Action Agent"
    environment: str = "development"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()