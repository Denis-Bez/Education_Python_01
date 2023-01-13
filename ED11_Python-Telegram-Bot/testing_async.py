import asyncio

from telegram.ext import ApplicationBuilder, Defaults, PicklePersistence
from telegram.ext import CommandHandler
from telegram import Update
from telegram.ext import ContextTypes

from config import BOT_KEY



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await asyncio.sleep(10)
    await update.message.reply_text(f"Hello, Hell!")

application = ApplicationBuilder().token(BOT_KEY).build()
application.add_handler(CommandHandler("start", start, block=False))

application.run_polling()    