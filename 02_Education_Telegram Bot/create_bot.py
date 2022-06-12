from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os

from config import token


# bot = Bot(token=os.getenv('TOKEN')) Этот вариант, если запускаем через bat файл
bot = Bot(token=token)
dp = Dispatcher(bot)