import asyncio

from app.bot import create_bot
from app.dispatcher import create_dispatcher
from app.logging import create_logger
from app.storage import create_storage


async def async_runner():
    bot = create_bot()
    logger = create_logger()
    storage = create_storage()
    dispatcher = create_dispatcher()
    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(async_runner())
