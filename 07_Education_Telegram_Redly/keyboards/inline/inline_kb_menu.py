from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


ikb_menu = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Сообщение', callback_data='Сообщение'),
                                        InlineKeyboardButton(text='Сылка', url='https://eg-expert.ru/')
                                    ],
                                    [
                                        InlineKeyboardButton(text='alert', callback_data='alert')
                                    ],
                                    [
                                        InlineKeyboardButton(text='Заменить инлайн кнопки', callback_data='Buttons_2')
                                    ]
                                ])