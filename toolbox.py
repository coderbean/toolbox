# coding=utf-8

from datetime import *
import time

print("Cmd/Ctrl + D to exit\n")
while True:
    try:
        arg = input('intput your timestap: ')
        if arg == '':
            print (">>>>>>当前时间：{} <<<<<<<".format(int(time.time())))
        else:
            print(datetime.fromtimestamp(int(arg)).strftime('%Y/%m/%d %H:%M:%S'))
    except EOFError:
        print("\nSee you next time.")
        break;
    except:
        print("check your input!!! \n")
