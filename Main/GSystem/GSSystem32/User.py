import os


class User:
    Infopath = None
    password = None
    username = None
    permissions = []
    
    def __init__(self, name, passw, perms, operative):
        if not operative:
            self.Create_User_File(name, passw, perms)
        else:
            self.Infopath = os.getcwd()+f'\\Main\\Users\\{name}\\User.txt'
            cont = open(self.Infopath, 'rt').read()
            self.password = cont[1].split(':')[1]
            self.username = cont[0].split(':')[1]
            self.GetPermissions()
    
    def GetPermissions(self):
        for permission in open(self.Infopath, 'rt').read()[2].split(':')[1].split(','):
            self.Add_Permission(permission)
    
    def Add_Permission(self,permission):
        if permission not in self.permissions:
            self.permissions.append(permission)

    def Create_User_File(self, getusername, getpassword, permissions):
        os.makedirs(f'{os.getcwd()}\\Main\\Users\\{getusername}\\Notes')
        file = open(os.getcwd()+ '\\Main\\Users\\'+getusername+'\\'+'User.txt', 'wt')
        file.write(f'login:{getusername}\npassword:{getpassword}\npermissions:{permissions}')
        
