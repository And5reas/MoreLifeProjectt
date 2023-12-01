import os
from sys import platform

# Fazer uma verificação rápida se existe o directório do programa
if platform == 'linux2':
    path_data_base = os.path.expanduser('~') + '\\MoreLife'
    if not os.path.isdir(path_data_base):
        os.mkdir(path_data_base)
elif platform == 'win32':
    path_data_base = os.path.expanduser('~') + '\\AppData\\Local\\MoreLife'
    if not os.path.isdir(path_data_base):
        os.mkdir(path_data_base)

import json

class dataBase:
    def __init__(self):
        self.pathDB = f"{path_data_base}\\Configuration.json"
        self.createJson()

    def createJson(self):
        if not os.path.exists(self.pathDB):
            table = {
                "resolution": "1024, 600",
                "theme": "Dark",
                "isLogged": False,
                "Timer1": "00:00:00;NOME",
                "Timer2": "00:00:00;NOME",
                "Timer3": "00:00:00;NOME",
                "Timer4": "00:00:00;NOME",
                "user_id": "",
            }
            obj_json = json.dumps(table, indent=2)
            with open(self.pathDB, "w") as file:
                file.write(obj_json)

    def saveConfig(self, atributo, contToSave):
        with open(self.pathDB, encoding='utf-8') as file:
            dataConfig = json.load(file)
            dataConfig[atributo] = contToSave
            dataConfig = json.dumps(dataConfig, indent=2)
        with open(self.pathDB, "w") as file:
            file.write(dataConfig)

    def loadConfig(self):
        with open(self.pathDB, encoding='utf-8') as file:
            dataConfig = json.load(file)
            return dataConfig
        
    def saveUserID(self, id):
        with open(self.pathDB, encoding='utf-8') as file:
            dataConfig = json.load(file)
            dataConfig['user_id'] = id
            dataConfig = json.dumps(dataConfig, indent=2)
        with open(self.pathDB, "w") as file:
            file.write(dataConfig)

    @staticmethod
    def getsaveUser():
        with open(f"{path_data_base}\\Configuration.json", encoding='utf-8') as file:
            dataConfig = json.load(file)
            return dataConfig['user_id']