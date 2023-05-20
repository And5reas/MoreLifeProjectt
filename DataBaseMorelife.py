import sqlite3
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


class MLDataBase:
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
                              "IsLogged INTEGER,"
                              "Timer1 TEXT, Timer2 TEXT, Timer3 TEXT, Timer4 TEXT);")
            self.conn.execute("INSERT INTO Config VALUES(NULL,?,?,?,?,?,?,?)", ("1024, 600", "Dark", 0, "00:00:00;NOME",
                                                                                "00:00:00;NOME", "00:00:00;NOME",
                                                                                "00:00:00;NOME"))
            self.conn.commit()
            self.conn.close()

    def save_db(self, colun, item_to_save):
        if item_to_save == 1 or item_to_save == 0:
            self.conn.execute(f"UPDATE Config SET {colun} = {item_to_save} WHERE ID = 1")
        elif ":" in item_to_save:
            self.conn.execute(f"UPDATE Config SET {colun} = '{item_to_save}' WHERE ID = 1")
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
