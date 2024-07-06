import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
from settings.config import TOKEN_BOT

# Set up logging for debugging (optional)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Define the echo function
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Echoes the user message."""
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

# Main function to start the bot
def main():
    """Starts the bot."""

    # Replace 'YOUR_BOT_TOKEN' with your actual bot token from BotFather
    application = ApplicationBuilder().token(TOKEN_BOT).build()

    # Add the echo handler
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    application.add_handler(echo_handler)

    # Start the bot
    application.run_polling()

# Execute the main function when the script is run
if __name__ == '__main__':
    main()