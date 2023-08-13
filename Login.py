import requests
import json

class confirmLogin:
    def __init__(self):
        self.link = "https://morelife-f4ffa-default-rtdb.firebaseio.com"

    def Check(self, email, senha):
        requisicao = requests.get(f"{self.link}/tb_user/.json")
        tb_user = requisicao.json()

        for id_user in tb_user:
            user_email = tb_user[id_user]["nm_email"]
            user_senha = tb_user[id_user]["nm_senha"]
            if user_email == email and user_senha == senha:
                return True
        return False