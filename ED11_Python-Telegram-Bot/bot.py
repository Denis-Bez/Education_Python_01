from config import TOKEN

import logging

from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler
from telegram.ext import InlineQueryHandler

from handlers import handlers

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)



if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    start_handler = CommandHandler('start', handlers.start)
    caps_handler = CommandHandler('caps', handlers.caps)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), handlers.echo)
    unknown_handler = MessageHandler(filters.COMMAND, handlers.unknown)
    inline_caps_handler = InlineQueryHandler(handlers.inline_caps)
    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    application.add_handler(caps_handler)
    application.add_handler(unknown_handler)
    application.add_handler(inline_caps_handler)
    
    application.run_polling()