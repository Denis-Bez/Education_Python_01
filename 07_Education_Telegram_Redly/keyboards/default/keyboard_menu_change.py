from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Second option menu
kb_menu_change = ReplyKeyboardMarkup(
    keyboard=[
        [
            # Three columns
            KeyboardButton(text='Инлайн меню'),
            KeyboardButton(text='Любой текс'),
            KeyboardButton(text='Лайк')
        ]
    ],
    resize_keyboard=True
)
