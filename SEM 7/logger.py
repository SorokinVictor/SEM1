from datetime import datetime as dt
from time import time


def logger(data):
    with open('log.csv', 'a') as file:
        file.write(f'\n{data}')
