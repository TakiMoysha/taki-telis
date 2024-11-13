from aiogram import Bot

from app.settings import get_settings

__all__ = ["create_bot"]


def create_bot():
    settings = get_settings()
    bot = Bot(settings.tel_token)
    return bot
