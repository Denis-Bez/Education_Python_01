import re
import time

import requests

#from config import IYUTEER
#import matplotlib.pyplot as plt
#import pandas as pd

menu = {
'rus': {
'dropmenu':[
{'dropdown_item': {'url': 'services', 'title': 'Услуги'}, 'items': [{'url': 'parsers', 'title': 'Разработка Парсеров'},
                                                                    {'url': 'telegram_bots', 'title': 'Разработка Telegram-ботов'},
                                                                    {'url': 'webapp', 'title': 'Создание веб-приложений'}]}
],
'menu':[
{'url': 'projects', 'title': 'Проекты'},
{'url': 'contacts', 'title': 'Контакты'}
]},

'eng': {
'dropmenu':[
{'dropdown_item': {'url': '.services', 'title': 'Services'}, 'items': [{'url': '.parsers', 'title': 'Development parsers'},
                                                                       {'url': '.telegram_bots', 'title': 'Development telegram-bots'},
                                                                       {'url': '.webapp', 'title': 'Create web-application'}]}
],
'menu':[
{'url': '.projects', 'title': 'Projects'},
{'url': '.contacts', 'title': 'Contacts'}
]}}

def main():
    m = {}
    m = menu['eng']

    for d in m['dropmenu'][0]['items']: 
        print(d['url'])

    





# Assing an arrey
""" def main():
    a = [1, 2]
    b, c = a
    print(f'b={b} c={c}') """


# Delite simbols in text
""" def main():
    a = ["     https://pythonstart.ru/string/strip-python", "fo  o", "bar      ", "bas"]

    a = [i.strip() for i in a]
    print(a) """

# Try Except
""" def main():
    a = 'Yohoo!'
    list = ['car', 1, 'feef', 'foo', 'bar', 'bas']

    try:
        a = list[6]
    except Exception as e:
	    print(e)
    finally:
	    print(a) """


# Decorators
""" def decorator (func):

    def inner():
        print('start decorator...')
        func()
        print('finish decorator...')
    
    return inner

def say():    
    print('Hello, Hell')

def main():
    say = 0
    say = decorator(say)
    print(say) """
    
    
if __name__ == "__main__":

# Помогает оценить скорость выполнения программы
    a = time.strftime('%X')

    main()

    b = time.strftime('%X')
    print(a)
    print(b)


