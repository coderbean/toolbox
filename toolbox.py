# coding=utf-8

from datetime import *
import time

print("Cmd/Ctrl + D to exit\n")
while True:
    try:
        arg = input('intput your timestap: ')
        print(datetime.fromtimestamp(int(arg)).strftime('%Y/%m/%d %H:%M:%S'))
    except EOFError:
        print("\nSee you next time.")
        break;
    except:
        print("check your input!!! \n")
