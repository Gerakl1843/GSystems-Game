import os
import Main.GSystem.GSSystem32.GGames.UnfairPong.UnfairPong as unp


def LaunchUnfairPong():
    unp.init()
    unp.mainloop()


def explore_system():
    currfold = input()
    show_system(currfold)


def show_system(current_folder):
    tree = os.walk('.')
    for i in tree:
        if current_folder == os.getcwd()+i[0].replace('.', ''):
            os.system('cls')
            print(i[1])


def GetCurrOpID(inp):
    curopID = 4
    for command in commands:
        if inp[0] == command[0]:
            curopID = command[1]
    return curopID


def GetError(inp):
    for command in commands:
        if inp[0] not in command:
            ErrID = 1
        else:
            ErrID = 0

    return ErrID


def prepare_data(ID, inp):
    if ID == 2:
        path = inp[1]
        try:
            mode = inp[2]
        except IndexError:
            mode = 'rt'
        res = [path, mode, ID]
    elif ID == 0:
        res = ['Goodbye!', 'nouse', ID]
    elif ID == 3:
        res = ['command', inp[1], ID]
    elif ID == 4:
        res = ['error', GetError(inp), ID]
    elif ID == 1:
        if inp[1] == 'UnfairPong':
            res = ['game', inp[1], ID]
    elif ID == 5:
        explore_system()
    else:
        return False

    return res


def openfilegetcont(path, mode='rt'):
    try:
        f = open(path, mode)
    except PermissionError:
        print('Access denied. This error isn\'t part of normal program functioning. \nThat means that program can\'t access given file.')
        f = open(os.getcwd() + '\\Main\\User\\System\\Notes\\Dummy.txt', 'rt')
    except FileNotFoundError:
        try:
            f = open(os.getcwd() + path, mode)
        except FileNotFoundError:
            print('Invalid Given path!')
            f = open(os.getcwd() + '\\Main\\User\\System\\Notes\\Dummy.txt', 'rt')
    try:
        cont = f.read()
    except UnicodeDecodeError:
        print('Can\'t open file due to incompatiable file format')
        f.close()
        f = open(os.getcwd() + '\\Main\\User\\System\\Notes\\Dummy.txt', 'rt')
        cont = f.read()
    f.close()
    return cont


def actions(prd):
    if prd[2] == 2:
        con = openfilegetcont(prd[0], prd[1])
        print('###########################################\n', con, '\n###########################################\n')
        return True
    elif prd[2] == 0:
        print(prd[0])
        return False
    elif prd[2] == 3:
        os.system(prd[1])
        return True
    elif prd[2] == 4:
        for error in errors:
            if prd[1] == error[1]:
                print('Error! ', error[0])
                return True
    elif prd[2] == 1:
        if prd[1] == 'UnfairPong':
            LaunchUnfairPong()


def mainloop():
    global errors
    errors = (('Command Not Available!', 1), ('Invalid argument syntax!', 2))
    global commands
    commands = (('exit', 0), ('run', 1), ('open', 2), ('command', 3), ('error', 4), ('explore', 5))
    run = True
    while run:
        x = input().split()
        curropid = GetCurrOpID(x)
        prd = prepare_data(curropid, x)
        run = actions(prd)
