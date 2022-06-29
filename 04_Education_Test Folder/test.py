import re
import time

import requests

#from config import IYUTEER
#import matplotlib.pyplot as plt
#import pandas as pd

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36', 'accept': '*/*'}

def main():

    # html = requests.get('https://www.intimshop.ru/klitoralnii_stimulyator_s_vibraciei_satisfyer_curvy_1_bordovii_o139028.html', headers=HEADERS, timeout=20)
    html = requests.get('https://www.ozon.ru/product/molochnaya-smes-kabrita-suhaya-na-osnove-kozego-moloka-dlya-detey-starshe-12-mesyatsev-800-g-160055585/?sh=yQWzKJ8lAw', headers=HEADERS, timeout=20)
    html = requests.get('https://www.ozon.ru/product/molochnaya-smes-friso-pep-1-s-rozhdeniya-400-g-299041548/', headers=HEADERS, timeout=20)
    html = requests.get('https://www.ozon.ru/product/molochnaya-smes-nestle-resource-clinutren-junior-zhidkaya-3-s-12-mesyatsev-so-vkusom-klubniki-200-g-189127875/?sh=yQWzKOGTIg', headers=HEADERS, timeout=20)
    html = requests.get('https://www.ozon.ru/product/molochnaya-smes-goattiny-2-na-osnove-kozego-moloka-dlya-detey-ot-6-do-12-mesyatsev-400g-191580017/?advert=yQLMamTjuIHN0w_66AfJq_66UiNtdv2QPxQ20X2nBNjnmueSiJFQkM_b3K0Oaau6Rn0MuiGiA-12CseE95rxwGM3jZRJcYQOytUk6KOnA_9USvVl0EuF643Xmg&sh=yQWzKBaQFA', headers=HEADERS, timeout=20)
    html = requests.get('https://www.ozon.ru/product/suhoy-molochnyy-napitok-dlya-detey-s-12-mesyatsev-bekari-3-na-osnove-ovechego-i-kozego-moloka-800-gr-309223318/?sh=yQWzKGNhDA', headers=HEADERS, timeout=20)

    # print(html)
    print(f'Выполнен 5 запросов к серверу сайта')
    





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


