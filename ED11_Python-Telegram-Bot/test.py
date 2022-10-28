import time

import requests
from bs4 import BeautifulSoup


HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36', 'accept': '*/*'}
URL = 'https://www.onlinetrade.ru/catalogue/sushilki_dlya_ovoshchey_i_fruktov-c312/kitfort/sushilka_dlya_ovoshchey_i_fruktov_kitfort_kt_1922-3034498.html'

def getSoup(self):
        for i in range(1, 3):
            try:
                html = requests.get(URL, headers=HEADERS)
                if html.status_code == 200:
                    soup = BeautifulSoup(html.text, 'html.parser')
                    items = soup.find('span', class_='js__actualPrice').get_text(strip=True)
                    return items
                return False
            except Exception as e:
                print(f"Something went wrong, {e}. Repeat {i}")
                time.sleep(i*15)          
        return False