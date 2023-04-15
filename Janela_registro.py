from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file('Resources/Janelas/login.kv')  # "Chamar" o arquivo kivy
Config.set('graphics', 'resizable', '0')  # Configurar a janela para não poder ser redimensionada
Config.set('graphics', 'width', '420')  # "Setar" a largura da janela
Config.set('graphics', 'height', '350')  # "Setar" a altura da janela


# Dedinir outra tela
class JanelaLogin(Screen):
    pass


class JanelaRegistrar(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class MyLayout(Widget):
    def btn_login(self):
        user_email = self.ids.email_input.text
        user_password = self.ids.password_input.text

        if "@" in user_email:
            self.ids.error_login.text = ""
            nome_user_email, domain_email = user_email.split("@")
            print(f"Nome do email: {nome_user_email}\nServidor: {domain_email}")
            print(f"Email: {user_email}\nSenha: {user_password}")
        else:
            self.ids.error_login.text = "Email e/ou senha inválido(s)"

        # Limpar TextInputs
        self.ids.email_input.text = ""
        self.ids.password_input.text = ""

    def btn_register(self):
        print("Ainda não funciona '-'")


class Login(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    Login().run()
