from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup

from app.settings import get_settings


router = Router()


@router.message(CommandStart())
async def start(msg: Message):
    await msg.answer(f"Hello, {msg.from_user.username}!")

    reply_keyboard_markup = ReplyKeyboardMarkup(resize_keyboard=True)
    reply_keyboard_markup.row(
        KeyboardButton("Start MiniApp", web_app=WebAppInfo(SETTINGS.tel_url))
    )

    inline_keyboard_markup = InlineKeyboardMarkup()
    inline_keyboard_markup.row(
        InlineKeyboardButton("Start MiniApp", web_app=WebAppInfo(SETTINGS.tel_url))
    )

    Bot.reply_to(
        msg,
        "Click the bottom inline button to start MiniApp",
        reply_markup=inline_keyboard_markup,
    )
    Bot.reply_to(
        msg,
        "Click keyboard button to start MiniApp",
        reply_markup=reply_keyboard_markup,
    )


@router.message(Command("info"))
async def user_info(msg: Message):
    await msg.answer(f"User ID: {msg.from_user.id}")


@router.message(Command("statistics"))
async def statistics(msg: Message):
    await msg.answer(f"Statistics: {msg.from_user.model_dump_json()}")


@router.message(Command("my_admin"))
async def my_admin(msg: Message):
    if msg.from_user.id != get_settings().owner_id:
        return await msg.answer("You are not admin")

    await msg.answer("setup...")
