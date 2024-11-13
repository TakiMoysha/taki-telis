from typing import Any, Awaitable, Callable, Dict
from aiogram import types
from aiogram import BaseMiddleware
from aiogram.dispatcher.event.handler import HandlerObject

DEFAULT_RATE_LIMIT = 4

type THandler = Callable[[types.TelegramObject, Dict[str, Any]], Awaitable[Any]]


def throttling(limit: int, key=None):
    def decorator(func):
        setattr(func, "throttling_rate_limit", key)
        if key:
            setattr(func, "throttling_key", key)
        return func

    return decorator


class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self, limit=DEFAULT_RATE_LIMIT, key_prefix="antiflood_"):
        self.rate_limit = limit
        self.prefix = key_prefix

        super(ThrottlingMiddleware, self).__init__()

    async def __call__(self, handler: THandler, event, data):
        if isinstance(event, types.Message):
            await self.on_process_message(handler, event, data)

        return await handler(event, data)

    async def on_process_message(
        self, handler: THandler, message: types.Message, data: dict
    ):
        dispatcher = Dispatcher.get_current()

        if handler:
            limit = getattr(handler, "throttling_rate_limit", self.rate_limit)
            key = getattr(handler, "throttling_key", f"{self.prefix}_{handler.__name__}")
        else:

try:
            await dispatcher.throttle(key, rate=limit)

        except Throttled as t:
            # Execute action

            await self.message_throttled(message, t)

            # Cancel current handler

            raise CancelHandler()

    async def message_throttled(self, message: types.Message, throttled: Throttled):
        """

        Notify user only on first exceed and notify about unlocking only on last exceed


        :param message:

        :param throttled:

        """

        handler = current_handler.get()

        dispatcher = Dispatcher.get_current()

        if handler:
            key = getattr(
                handler, "throttling_key", f"{self.prefix}_{handler.__name__}"
            )

        else:
            key = f"{self.prefix}_message"

        # Calculate how many time is left till the block ends

        delta = throttled.rate - throttled.delta

        # Prevent flooding

        if throttled.exceeded_count <= 2:
            await message.reply("Too many requests! ")

        # Sleep.

        await asyncio.sleep(delta)

        # Check lock status

        thr = await dispatcher.check_key(key)

        # If current message is not last with current key - do not send message

        if thr.exceeded_count == throttled.exceeded_count:
            await message.reply("Unlocked.")
