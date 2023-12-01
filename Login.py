import requests

class confirmLogin:
    def __init__(self):
        self.link = "https://morelife-f4ffa-default-rtdb.firebaseio.com"

    def Check(self, email, senha, DBML):
        requisicao = requests.get(f"{self.link}/tb_user/.json")
        tb_user = requisicao.json()

        for id_user in tb_user:
            user_email = tb_user[id_user]["nm_email"].lower()
            user_senha = tb_user[id_user]["nm_senha"]
            if user_email == email.lower() and user_senha == senha:
                DBML.saveUserID(id_user)
                return True
        return False