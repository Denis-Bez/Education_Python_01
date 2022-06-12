from aiogram import types, Dispatcher
from create_bot import dp

import json, string


# Пустой хендлер необходимо писать в самом низу, т.к. они обрабатываются сверху вниз
#@dp.message_handler()
async def other_handler(message: types.Message): # Событие - "сообщение в чат"   
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

def register_handler_other(dp: Dispatcher): # 'dp: Dispatcher' - аннотация типов
    dp.register_message_handler(other_handler)