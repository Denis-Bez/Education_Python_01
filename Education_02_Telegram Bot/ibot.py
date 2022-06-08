from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

@dp.message_handler()
async def echo_send(message: types.Message): # Событие - "сообщение в чат"
    if message.text.lower() == 'привет':
        await message.answer('Забор покрасьте!')
    elif message.text.lower() == 'здрасте':
        await message.answer('Лоха ответ!')
    
    # await message.answer(message.text) # Отправляет полученнок сообщение в ответ
    # await message.reply(message.text) # Отправляет полученнок сообщение в ответ (с цитированием)
    # await bot.send_message(message.from_user.id, message.text) # Ответ непосредственно в личку пользователю (бот первый пользователю написать не может). Получаем id пользователя

executor.start_polling(dp, skip_updates=True) # "skip_updates=True" чтобы бот после оффлайна не отвечал на все присланные сообщения"