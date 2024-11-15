from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.base import BaseStorage

from .routers import router

__all__ = ["create_dispatcher"]


def create_dispatcher(
    bot: Bot | None = None,
    storage: BaseStorage | None = None,
    *args,
    **kwargs,
):
    dp = Dispatcher(bot=bot, storage=storage, *args, **kwargs)
    dp.include_router(router)
    return dp
