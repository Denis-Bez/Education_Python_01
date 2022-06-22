from aiogram import types

# Create menu and discriptions
async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Запуск бота'),
        types.BotCommand('help', 'Помощь балбесам'),
        types.BotCommand('menu', 'Меню бота'),
    ])