from loader import dp
from states import register

from aiogram import types
from aiogram.dispatcher.filters import Command

# /register (Starting registration)
@dp.message_handler(Command('register')) 
async def register(message: types.Message):
    await message.answer('Привет, ты начал регистрацию, \nВведи своё имя:')
    await register.register1.set() # Set first state

# Catch all message users in first state (State of inputing name)
@dp.message_handler(state=register.register1)
async def state1(message: types.Message):
    # 5.29 (https://www.youtube.com/watch?v=A2fnlJJ4Pl4&list=PLPELDof3v08efHGT3gVLPCXG5cKRo50Nn&index=6)
