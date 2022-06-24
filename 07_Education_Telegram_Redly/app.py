# Coommand to be executed on startup
async def on_startup(dp):

    import filters
    filters.setup(dp)

    import middlewares
    middlewares.setup(dp)

    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)

    from utils.set_bot_commands import set_default_commands
    await set_default_commands(dp)

    print('Бот запущен')

# Startup bot
if __name__ == '__main__':
    from aiogram import executor

    # Version from without __init__
    # from handlers.users.start import dp
    # from handlers.users.help import dp
    # ...

    # Version with __init__
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)