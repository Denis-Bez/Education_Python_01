from telegram import Update
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import ContextTypes, JobQueue
from telegram.constants import ParseMode

import pytz
import datetime as dtm
from uuid import uuid4


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):    
    # First message (echo)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
    # Second message (you say...)
    await update.message.reply_text("You said: " + update.message.text)


async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


async def inline_caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.inline_query.query
    if not query:
        return
    results = []
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='CAPS',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    await context.bot.answer_inline_query(update.inline_query.id, results)


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")


# --- Demonstration of temporary save data and extraction  ---
async def put(update, context):
    """Usage: /put value"""
    # Generate ID and separate value from command
    key = str(uuid4())
    # We don't use context.args here, because the value may contain whitespaces
    value = update.message.text.partition(' ')[2]

    # Store value
    context.user_data[key] = value
    # Send the key to the user
    await update.message.reply_text(key)


async def get(update, context):
    """Usage: /get uuid"""
    # Separate ID from command
    key = context.args[0]

    # Load value and send it to the user
    value = context.user_data.get(key, 'Not found')
    await update.message.reply_text(value)

# --- Demonstration of default setting Application and work of Schedule---
async def job(context):
    chat_id = context.job.chat_id
    timezone = context.bot.defaults.tzinfo
    local_now = dtm.datetime.now(timezone)
    utc_now = dtm.datetime.utcnow()
    text = f'Running job at {local_now} in timezone {timezone}, which equals {utc_now} UTC.'
    await context.bot.send_message(chat_id=chat_id, text=text)


async def echo(update, context):
    text = update.message.text
    # Send with default parse mode
    await update.message.reply_text(f'<b>{text}</b>')
    # Override default parse mode locally
    await update.message.reply_text(f'*{text}*', parse_mode=ParseMode.MARKDOWN)
    # Send with no parse mode
    await update.message.reply_text(f'*{text}*', parse_mode=None)

    # Schedule job (Default timezone = Moscow)
    context.job_queue.run_once(
        job, dtm.datetime.now() - dtm.timedelta(seconds=7180), chat_id=update.effective_chat.id
    )

# --- Repeat message every minute ---
async def callback_minute(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id='@edbotchan', text='One message every minute')
