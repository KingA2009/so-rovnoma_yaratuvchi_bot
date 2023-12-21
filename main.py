import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import ParseMode
from aiogram.utils import executor
from aiogram.utils.exceptions import BotBlocked
from config import API_TOKEN

logging.basicConfig(level=logging.DEBUG )

bot = Bot(token=API_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(CommandStart())
async def start(message: types.Message):
    keyboard2 = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    btns = ["Ozbek", "Rus", "Ingiliz"]
    for btn in btns:
        keyboard2.insert(types.KeyboardButton(text=btn))
    await message.answer(
        text=f'Salom <em>{message.from_user.full_name}</em>!, Hello <em>{message.from_user.full_name}</em>!, Привет <em>{message.from_user.full_name}</em>!. Tilni Tanlang, Выберите язык, Select the language',
        reply_markup=keyboard2
    )

@dp.message_handler(content_types="text")
async def echo(message: types.Message):
    language =message.text.lower()
    msg = ""
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    if language == "ozbek":
        msg = "Siz o`zbek tilini tanladingiz"
        keyboard.add(types.KeyboardButton(text='So`rovnoma Yaratish',
                                          request_poll=types.KeyboardButtonPollType(type=types.PollType.REGULAR)))
        keyboard.add(types.KeyboardButton(text='Quiz Yaratish',
                                          request_poll=types.KeyboardButtonPollType(type=types.PollType.QUIZ)))
    elif language == "rus":
        msg = "Вы выбрали русский язык"
        keyboard.add(types.KeyboardButton(text='Создание опроса',
                                          request_poll=types.KeyboardButtonPollType(type=types.PollType.REGULAR)))
        keyboard.add(types.KeyboardButton(text='Создать тест',
                                          request_poll=types.KeyboardButtonPollType(type=types.PollType.QUIZ)))
    elif language == "ingiliz":
        msg = "You selected english language"
        keyboard.add(types.KeyboardButton(text='Creating a survey',
                                          request_poll=types.KeyboardButtonPollType(type=types.PollType.REGULAR)))
        keyboard.add(types.KeyboardButton(text='Creating a quiz',
                                          request_poll=types.KeyboardButtonPollType(type=types.PollType.QUIZ)))
    await message.answer(
        text=msg,
        reply_markup=keyboard
    )

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp)
