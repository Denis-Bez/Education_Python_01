from main import bot, dp

from aiogram.types import Message
from config import ADMIN_ID

async def send_to_admin(dp):
    await bot.send_message(chat_id=ADMIN_ID, text='Бот запущен')