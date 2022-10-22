from email import message
from telegram import Update
from telegram import InlineKeyboardButton, ReplyKeyboardMarkup
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import ApplicationHandlerStop
from telegram.ext import ContextTypes, JobQueue
from telegram.constants import ParseMode

import pytz
import datetime as dtm
from time import time
from uuid import uuid4

from typing import Union, List

from models.model import Bot_db


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


# async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):    
#     # First message (echo)
#     await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
#     # Second message (you say...)
#     await update.message.reply_text("You said: " + update.message.text)


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


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    # Override default parse mode locally
    await update.message.reply_text(f'*{text}*', parse_mode=ParseMode.MARKDOWN)
    # Send with no parse mode
    # await update.message.reply_text(f'*{text}*', parse_mode=None)

    # Schedule job (Default timezone = Moscow)
    # context.job_queue.run_once(
    #     job, dtm.datetime.now() - dtm.timedelta(seconds=7180), chat_id=update.effective_chat.id
    # )

# --- Repeat message every minute ---
async def callback_minute(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id='@edbotchan', text='One message every minute')


# --- Add jobs in response to certain user input ---
async def callback_alarm(context: ContextTypes.DEFAULT_TYPE):
    # Beep the person who called this alarm:
    await context.bot.send_message(chat_id=context.job.chat_id, text=f'BEEP {context.job.data}!')
 
 
async def callback_timer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    name = update.effective_chat.full_name
    await context.bot.send_message(chat_id=chat_id, text='Setting a timer for 1 minute!')
    # Set the alarm:
    context.job_queue.run_once(callback_alarm, 60, data=name, chat_id=chat_id)


# -- Use SQLAlchemy ---
async def sql(update: Update, context: ContextTypes.DEFAULT_TYPE):
    Bot_db.add_user(update.effective_chat.id, update.effective_message.text)
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Dates was added to database!')


# --- Handle updates in several handlers. Simple spam-filter ---
async def typehandler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Bot_db.add_user(update.effective_chat.id, update.effective_message.text)
    MAX_USAGE = 5
    count = context.user_data.get("usageCount", 0)
    restrict_since = context.user_data.get("restrictSince", 0)

    if restrict_since:
        if (time() - restrict_since) >= 60 * 5: # 5 minutes
            del context.user_data["restrictSince"]
            del context.user_data["usageCount"]
            await update.effective_message.reply_text("I have unrestricted you. Please behave well.")
        else:
            await update.effective_message.reply_text("Back off! Wait for your restriction to expire...")
            raise ApplicationHandlerStop
    else:
        if count == MAX_USAGE:
            context.user_data["restrictSince"] = time()
            await update.effective_message.reply_text("Stop flooding! Don't bother me for 5 minutes...")
            raise ApplicationHandlerStop
        else:
            context.user_data["usageCount"] = count + 1

# Build menu with buttons
async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    custom_keyboard = [['top-left', 'top-right'], 
                      ['bottom-left', 'bottom-right']]
    reply_markup = ReplyKeyboardMarkup(custom_keyboard)
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text="Custom Keyboard Test", 
        reply_markup=reply_markup
        )