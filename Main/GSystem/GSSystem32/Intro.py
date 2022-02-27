import os
import time


def intro():
    success = False
    f = open(os.getcwd()+'\\SysFiles\\Intro.txt')
    cont = f.read().split('\n')
    print(cont[0])
    time.sleep(5)
    for i in range(0,89):
        print(cont[1]+str(i))
        time.sleep(0.06)
    print(cont[2])
    time.sleep(2)
    print(cont[3])
    time.sleep(3)
    print(cont[4])
    time.sleep(3)
    print(cont[5])
    time.sleep(5)
    for i in range(0,101):
        print(cont[6]+str(i))
        time.sleep(0.07)
    for i in range(0,101):
        print(cont[7]+str(i))
        time.sleep(0.02)
    while success is False:
        success = decide(cont)


def decide(cont):
    option = input(cont[8]+'\n')
    if option == 'Y':
        for i in range(0,45):
            print('Moving old user...'+str(i))
            time.sleep(0.08)
        print(cont[9])
    elif option == 'n':
        pass
    else:
        return False