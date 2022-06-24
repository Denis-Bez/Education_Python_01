from unicodedata import name
from loader import dp
from states import register
from keyboards.default import kb_menu

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# /register (Starting registration)
@dp.message_handler(Command('register')) 
async def register_start(message: types.Message):
    # Keybort with username buttons
    name = ReplyKeyboardMarkup(
        keyboard=[
        [
            KeyboardButton(text=f'{message.from_user.first_name}'),
        ]
        ],  resize_keyboard=True
    )

    await message.answer('Привет, ты начал регистрацию, \nВведи своё имя:', reply_markup=name)
    await register.register1.set() # Set first state

# Catch all message users in first state (State of inputing name)
@dp.message_handler(state=register.register1)
async def register_state1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(register1=answer)
    await message.answer(f'{answer} Сколько тебе лет?')
    await register.register2.set() # Set second state


@dp.message_handler(state=register.register2)
async def register_state2(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(register2=answer)
    data = await state.get_data()
    await message.answer(f'Регистрация успешно завершена\n'
                        f'Твоё имя {data["register1"]} \n'
                        f'Тебе {data["register2"]} лет', reply_markup=kb_menu)

    await state.finish()