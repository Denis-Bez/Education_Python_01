import asyncio

from aiogram import types, executor, Dispatcher, Bot

from config import TOKEN_BOT


bot = Bot(token=TOKEN_BOT)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def begin(message: types.Message):
    await bot.send_message(message.chat.id, 'Hello, Hell!')


@dp.message_handler(content_types=['text'])
async def text(message: types.Message):
    await asyncio.sleep(20)
    await bot.send_message(message.chat.id, 'It worked!')


executor.start_polling(dp)