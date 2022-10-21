from uuid import uuid4

import pytz
import datetime

def b():
    # key = str(uuid4())
        moscowZone = datetime.datetime.now(pytz.timezone('Europe/Moscow'))
        print(moscowZone)
        print(moscowZone.astimezone(pytz.timezone('Asia/Dhaka')))


if __name__ == '__main__':
    b()