from aiogram import Bot, Dispatcher, executor
from config import BOT_TOKEN


bot = Bot(BOT_TOKEN, parse_mode='HTML') # Принцип форматирования текста, как в HTML (Есть ещё Markdown)
dp = Dispatcher(bot) # Обработчик и доставщик

# Если имя этого файла 'main'. Т.е. мы как бы изолируем при импортировании код ниже этой надписи
if __name__ == '__main__':
    from handlers import dp, send_to_admin
    executor.start_polling(dp, on_startup=send_to_admin) # Функция которая делает запросы getUpdates и передает их в Dispatcher. При запуске выполняет функцию send_to_admin

