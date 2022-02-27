from System import *
from User import User
import os
import Intro

Users = []


def Login():
    z = 0
    currUser = None
    tree = os.walk('.')
    username = input('Enter Username: ')
    password = input('Enter Password: ')
    for i in tree:
        if i[0] == '.\\Main\\Users':
            for j in i[1]:
                with open(os.getcwd() + i[0].replace('.', '') + '\\' + j + '\\User.txt') as f:
                    cont = f.read()
                    Lis = [cont.split('\n')[0].split(':')[1], cont.split('\n')[1].split(':')[1]]
                    Users.append([])
                    Users[z] = Lis
                    z += 1
            break
    for user in Users:
        if user[0] == username and user[1] == password:
            currUser = user[0]
    if currUser is None:
        return False
    return currUser


def register():
    global NewUser
    NewUser = None
    tree = os.walk('.')
    z = 0
    for i in tree:
        if i[0] == '.\\Main\\Users':
            for j in i[1]:
                with open(os.getcwd() + i[0].replace('.', '') + '\\' + j + '\\User.txt') as f:
                    cont = f.read()
                    Lis = [cont.split('\n')[0].split(':')[1], cont.split('\n')[1].split(':')[1]]
                    Users.append([])
                    Users[z] = Lis
                    z += 1
            break
    name = input(
        'Enter your username. It can be whatever you want. Just make sure it does not contain any personal info, \nbecause it will be used as your name in our GGames system!\n')
    password = input('Now your password! Remember: do not tell it to anyone. We won\'t!\n')
    permissions = 'user'
    print(
        'Oops! Seems like you\'re not the first who\'s using this device. So you\'ll be just a user. \nBut do not worry, we think if you will ask admin\npolitely, he(she) will make you admin too!\n')
    for user in Users:
        if user[0] != name:
            NewUser = User(name, password, permissions, False)
    if NewUser is not None:
        return NewUser
    else:
        print('User already exists')


def UpdateUserList(Usr):
    with open(os.getcwd() + '\\Users\\Users.txt', 'rt') as f1:
        cont = f1.read()
        cont = cont[0].split(',')
    with open(os.getcwd() + '\\Users\\Users.txt', 'wt') as f1:
        for i in cont:
            if i not in Users:
                f1.write(',' + i)
    if Usr not in Users:
        f1.write(',' + Usr)
    f1.close()


def start():
    if input('Press any button\n') != 'skip':
        Intro.intro()
    option = input('Hello User! Choose operation. Login/Register.\n')
    if option == 'Login':
        if Login() is not False:
            mainloop()
        else:
            print('Invalid Username or password!\n')
    elif option == 'Register':
        NUser = register()
        if NUser is not None:
            UpdateUserList(NUser)
        else:
            print('Error')


start()
