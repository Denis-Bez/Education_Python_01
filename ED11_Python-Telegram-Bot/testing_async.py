import asyncio

from telegram.ext import ApplicationBuilder, Defaults, PicklePersistence
from telegram.ext import CommandHandler
from telegram import Update
from telegram.ext import ContextTypes

from config import BOT_KEY

application = ApplicationBuilder().token(BOT_KEY).build()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await asyncio.sleep(20)
    await update.message.reply_text(f"Hello, Hell!")


application.add_handler(CommandHandler("start", start))


if __name__ == '__main__':  
    application.run_polling()