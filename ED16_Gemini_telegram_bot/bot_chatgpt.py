from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

from settings.config import TOKEN

# Function to start the bot
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hi! I am an Echo Bot. Send me any message, and I will echo it back!')

# Function to echo received messages
def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

# Function to handle errors
def error(update: Update, context: CallbackContext) -> None:
    print(f'Update {update} caused error {context.error}')

def main():
    # Create the Updater and pass it your bot's token
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # On different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))

    # On non-command messages - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Log all errors
    dispatcher.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()