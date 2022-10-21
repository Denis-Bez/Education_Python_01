from config import TOKEN

from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, Defaults, Application
from telegram.ext import InlineQueryHandler
from telegram.constants import ParseMode

from handlers import handlers
import pytz

defaults = Defaults(parse_mode=ParseMode.HTML, tzinfo=pytz.timezone('Europe/Moscow'))

# application = ApplicationBuilder().token(TOKEN).build()

application = (
    Application.builder()
    .token(TOKEN)
    .defaults(defaults)
    .build()
)

# Command handlers
application.add_handler(CommandHandler('start', handlers.start))
application.add_handler(CommandHandler('caps', handlers.caps))
application.add_handler(CommandHandler('put', handlers.put))
application.add_handler(CommandHandler('get', handlers.get))


# Message handlers
unknown_handler = MessageHandler(filters.COMMAND, handlers.unknown)
# application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handlers.echo))
application.add_handler(unknown_handler)
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handlers.echo))

# Inline handlers
inline_caps_handler = InlineQueryHandler(handlers.inline_caps)
application.add_handler(inline_caps_handler)

# Job queue
job_queue = application.job_queue
job_minute = job_queue.run_repeating(handlers.callback_minute, interval=60, first=10)
job_minute.enabled = False  # Temporarily disable this job