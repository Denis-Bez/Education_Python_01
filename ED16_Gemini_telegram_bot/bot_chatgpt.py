from telegram.ext import Updater, MessageHandler, Filters

from settings.config import TOKEN

# Define a function to echo messages
def echo(update, context):
    # Get the message from the user
    text = update.message.text
    # Send the same message back to the user
    update.message.reply_text(text)

def main():
    # Create the Updater and pass in the bot's token
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Define a message handler for the /echo command
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dp.add_handler(echo_handler)

    # Start the Bot
    updater.start_polling()
    print('Bot is running! Press Ctrl+C to exit.')

    # Run the bot until you press Ctrl+C
    updater.idle()

if __name__ == '__main__':
    main()