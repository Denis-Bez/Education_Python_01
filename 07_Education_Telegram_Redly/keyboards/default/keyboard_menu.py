from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Create visual menu
kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        # Row 1
        [
            # Two columns
            KeyboardButton(text='10'),
            KeyboardButton(text='1')
        ],
        # Row 2
        [
            # One columns
            KeyboardButton(text='100') 
        ],
        # Row 3
        [
            # Three columns
            KeyboardButton(text='Инлайн меню'),
            KeyboardButton(text='Любой текс'),
            KeyboardButton(text='Лайк')
        ]
    ],
    resize_keyboard=True # Adapts size buttons
)
