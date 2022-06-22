from loader import dp
from aiogram import types
from aiogram.types import CallbackQuery

from keyboards.inline import ikb_menu
from keyboards.inline import ikb_menu2
from keyboards.default import kb_menu_change

@dp.message_handler(text='Инлайн меню')
async def show_inline_menu(message: types.Message):
    await message.answer('Инлайн меню ниже', reply_markup=ikb_menu)


@dp.callback_query_handler(text='Сообщение')
async def send_message(call: CallbackQuery):
    await call.message.answer('Кнопки заменены', reply_markup=kb_menu_change)


@dp.callback_query_handler(text='alert')
async def send_alert(call: CallbackQuery):
    # await call.answer('Кнопки заменены') # First version of notification
    await call.answer('Кнопки заменены', show_alert=True) # Second version of notification


@dp.callback_query_handler(text='Buttons_2')
async def Buttons_2(call: CallbackQuery):
    await call.message.edit_reply_markup(ikb_menu2) # Edit previous menu

