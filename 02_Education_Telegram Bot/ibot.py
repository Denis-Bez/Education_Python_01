from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from click import command
from config import token

import os, json, string


# bot = Bot(token=os.getenv('TOKEN')) Этот вариант, если запускаем через bat файл
bot = Bot(token=token)
dp = Dispatcher(bot)

async def on_startup(_):
    print('Бот вышел в онлайн')

# КЛИЕНТСКАЯ ЧАСТЬ
@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита')
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему: \nhttps://t.me/botethusdtprice_bot')

@dp.message_handler(commands=['Режим_работы'])
async def pizza_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вс-Чт с 9:00 до 20:00, Пт-Сб с 10:00 до 23:00')

@dp.message_handler(commands=['Расположение'])
async def pizza_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'ул. Колбасная 15')


# Пустой хендлер необходимо писать в самом низу, т.к. они обрабатываются сверху вниз
@dp.message_handler()
async def echo_send(message: types.Message): # Событие - "сообщение в чат"   
    # await message.answer(message.text) # Отправляет полученное сообщение в ответ
    # await message.reply(message.text) # Отправляет полученнок сообщение в ответ (с цитированием)
    # await bot.send_message(message.from_user.id, message.text) # Ответ непосредственно в личку пользователю (бот первый пользователю написать не может). Получаем id пользователя

    # Фильтр мата. Используем генератор множеств
    # (str.maketrans(<что менять>, <на что менять>, <что удалить>) - метод обработки строки, убираем маскирующие символы
    # мы можем очень быстро сравнить два множества методом пересечения множеств
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('cenz.json')))) != set():
        await message.reply('Маты запрещены')
        await message.delete()

executor.start_polling(dp, skip_updates=True, on_startup=on_startup) # "skip_updates=True" чтобы бот после оффлайна не отвечал на все присланные сообщения"