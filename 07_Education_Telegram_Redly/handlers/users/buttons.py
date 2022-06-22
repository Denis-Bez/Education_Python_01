from aiogram import types
from loader import dp

# Catch and answer button values
@dp.message_handler(text=['10', '100', '1'])
async def buttons_test(message: types.Message):
    await message.answer(f'Привет {message.from_user.full_name}! \n'
                        f'Ты выбрал число: {message.text}')