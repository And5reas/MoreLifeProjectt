import sqlite3
import os
from sys import platform

import LoadProgramStuffs

# Fazer uma verificação rápida se existe o directório do programa
if platform == 'linux2':
    path_data_base = os.path.expanduser('~') + '\\MoreLife'
    if not os.path.isdir(path_data_base):
        os.mkdir(path_data_base)
elif platform == 'win32':
    path_data_base = os.path.expanduser('~') + '\\AppData\\Local\\MoreLife'
    if not os.path.isdir(path_data_base):
        os.mkdir(path_data_base)


class ConfigDataBase:
    conn = None
    cursor = None

    def __init__(self):
        pass

    def create_db(self):
        if not os.path.exists(path_data_base + "\\Configuration.db"):
            self.conn = sqlite3.connect(path_data_base + "\\Configuration.db")
            self.conn.execute("CREATE TABLE IF NOT EXISTS Config"
                              "(ID INTEGER PRIMARY KEY AUTOINCREMENT,"
                              "Resolution TEXT,"
                              "Teme TEXT,"
                              "IsLogged INTEGER);")
            self.conn.execute("INSERT INTO Config VALUES(NULL,?,?,?)", ("1024, 600", "Dark", 0))
            self.conn.commit()
            self.conn.close()

    def save_config(self, colun, item_to_save):
        if item_to_save == 'FullScreen':
            w, h = LoadProgramStuffs.WindowInformation.get_window_size()
            item_to_save = str(w) + ', ' + str(h)
        if item_to_save is not str:
            self.conn.execute(f"UPDATE Config SET {colun} = {item_to_save} WHERE ID = 1")
        else:
            self.conn.execute(f"UPDATE Config SET {colun} = '{item_to_save}' WHERE ID = 1")

    def load_config(self):
        self.start_connection()
        self.cursor.execute('SELECT * FROM Config WHERE ID = 1')
        lista = self.cursor.fetchall()  # Retorna uma lista da config
        self.conn.close()
        self.cursor = None
        return lista

    def commit_and_close(self):
        self.conn.commit()
        self.cursor = None
        self.conn.close()

    def start_connection(self):
        self.conn = sqlite3.connect(path_data_base + "\\Configuration.db")
        if self.cursor is None:
            self.cursor = self.conn.cursor()
