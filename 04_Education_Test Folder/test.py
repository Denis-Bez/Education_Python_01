import re
import time

import requests

#from config import IYUTEER
#import matplotlib.pyplot as plt
#import pandas as pd


def main():
    n = 3
    m = 2
    sum = 0

    for n in range(n, 0, -1):
        for m in range(m, 0, -1):
            if n > 1:
                sum += 1
            if m > 1:
                sum += 1
    
    print(sum)



    

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


