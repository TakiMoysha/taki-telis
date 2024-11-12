import os

from dotenv import load_dotenv

from telebot import TeleBot
from telebot.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    WebAppInfo,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)


load_dotenv()

TOKEN = str(os.getenv("TELEGRAM_BOT_TOKEN"))
URL = str(os.getenv("TELEGRAM_BOT_URL"))

Bot = TeleBot(TOKEN)


@Bot.message_handler(commands=["start"])
def start(message):
    reply_keyboard_markup = ReplyKeyboardMarkup(resize_keyboard=True)
    reply_keyboard_markup.row(KeyboardButton("Start MiniApp", web_app=WebAppInfo(URL)))

    inline_keyboard_markup = InlineKeyboardMarkup()
    inline_keyboard_markup.row(
        InlineKeyboardButton("Start MiniApp", web_app=WebAppInfo(URL))
    )

    Bot.reply_to(
        message,
        "Click the bottom inline button to start MiniApp",
        reply_markup=inline_keyboard_markup,
    )
    Bot.reply_to(
        message,
        "Click keyboard button to start MiniApp",
        reply_markup=reply_keyboard_markup,
    )


@Bot.message_handler(content_types=["web_app_data"])
def web_app(message):
    Bot.reply_to(message, f'Your message is "{message.web_app_data.data}"')


if __name__ == "__main__":
    print("RUN")
    Bot.infinity_polling()
