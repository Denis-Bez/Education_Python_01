# Пример бота без использования специализированных библиотек
import requests

API_LINK = 'https://api.telegram.org/bot5404436374:AAFwSx1GU7GQGPAG-sLjtyJ1zxhcOoVVv2c'

# Получаем в ответ на запрос get json файл и преобразовываем его в словарь
updates = requests.get(API_LINK + '/getUpdates?offset=-1').json()

message = updates['result'][0]['message']
# Забираем из полученного ответа id чата и текст сообщения
chat_id = message['from']['id']
text = message['text']

# Отправляем ответ пользователю
send_message = requests.get(API_LINK + f'/sendMessage?chat_id={chat_id}&text=Эййй..пс, привет')

print(send_message)