from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings

from app.types import TelegramToken


class Settings(BaseSettings):
    owner_id: str = Field(default=..., alias="TELEGRAM_OWNER_ID")
    tel_token: TelegramToken = Field(default=..., alias="TELEGRAM_BOT_TOKEN")
    tel_url: str = Field(default=..., alias="TELEGRAM_BOT_URL")

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()
