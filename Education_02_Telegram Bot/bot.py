import requests
from datetime import datetime
from config import token
import telebot


def get_data():
    req = requests.get('https://yobit.net/api/3/ticker/eth_usdt')
    response = req.json()
    buy_price = response['eth_usdt']['buy']
    
    return f'{datetime.now().strftime("%Y-%m-%d %H:%M")}\nBuy ETH price: {round(buy_price)} USDT'


def telegram_bot(token):
    bot = telebot.TeleBot(token)
    
    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, 'Hello, friend! Write the "price" to find out the cost of ETH!')
    
    
    @bot.message_handler(content_types=['text'])
    def send_text(message):
        if message.text.lower() == 'price':
            try:
                quote = get_data()
                bot.send_message(message.chat.id, quote)
            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id, 
                    'Damn...Someting was wrong...')
        else:
            bot.send_message(message.chat.id, 'What??? Check the command dude!')

    bot.polling()
    
 
if __name__ == '__main__':
    telegram_bot(token)
