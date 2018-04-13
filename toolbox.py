# coding=utf-8

from datetime import *
import time

while True:
    arg = input('intput your timestap: ')
    print(datetime.fromtimestamp(int(arg)).strftime('%Y/%m/%d %H:%M:%S'))
