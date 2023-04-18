from kivy.config import Config
Config.set('graphics','resizable',0)

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
import sys

# Checar qual o tamanho do monitor do usuário
if sys.platform == 'linux2':
    import subprocess
    output = subprocess.Popen(
        'xrandr | grep "\*" | cut -d" " -f4',
        shell=True,
        stdout=subprocess.PIPE).communicate()[0]
    screen_x = int(output.replace('\n', '').split('x')[0])
    screen_y = int(output.replace('\n', '').split('x')[1])
elif sys.platform == 'win32':
    from win32api import GetSystemMetrics
    screen_x = GetSystemMetrics(0)
    screen_y = GetSystemMetrics(1)
else:
    # For mobile devices, use full screen
    screen_x, screen_y = 800, 600  # return something


def center_window(size_x, size_y):
    Window.size = (size_x, size_y)
    Window.left = (screen_x - size_x) / 2
    Window.top = (screen_y - size_y) / 2


# Dedinir outra tela
class JanelaLogin(Screen):
    checar = True
    def btn_login(self):
        user_email = self.ids.email_input.text
        user_password = self.ids.password_input.text

        if "@" in user_email:
            self.ids.error_login.text = ""
            nome_user_email, domain_email = user_email.split("@")
            print(f"Nome do email: {nome_user_email}\nServidor: {domain_email}")
            print(f"Email: {user_email}\nSenha: {user_password}")
            if nome_user_email == "Andreas" and user_password == "batata123":
                return True
        else:
            self.ids.password_input.background_color = (212/255, 25/255, 32/255, .6)
            self.ids.email_input.background_color = (212/255, 25/255, 32/255, .6)
            self.ids.error_login.text = "Email e/ou senha inválido(s)"
        return False

    def validate_color(self):
        if self.ids.password_input.background_color != (1, 1, 1, 1):
            self.ids.password_input.background_color = (1, 1, 1, 1)
        if self.ids.email_input.background_color != (1, 1, 1, 1):
            self.ids.email_input.background_color = (1, 1, 1, 1)

    def on_pre_enter(self):
        center_window(420, 350)

    def remove_password_mask(self):
        if not self.checar:
            self.checar = True
            self.ids.eye_password_mask.source = "Resources\Imgs\ZoioFechado.png"
        else:
            self.checar = False
            self.ids.eye_password_mask.source = "Resources\Imgs\ZoioAberto.png"
        self.ids.password_input.password = self.checar

    def keep_login(self, ref=0):
        if ref == 1:
            self.ids.check_keep_login.active = True


class JanelaRegistrar(Screen):
    def cadastrar(self):
        nome = self.ids.user_name.text
        email = self.ids.email_register.text
        senha = self.ids.password_register.text
        senha_comfirmar = self.ids.password_confirm_register.text
        if senha != senha_comfirmar:
            self.ids.password_register.background_color = (212/255, 25/255, 32/255, .6)
            self.ids.password_confirm_register.background_color = (212 / 255, 25 / 255, 32 / 255, .6)
        elif "@" not in email:
            self.ids.email_register.background_color = (212 / 255, 25 / 255, 32 / 255, .6)
        else:
            print(nome, email, senha, senha_comfirmar)

    def validate_color(self):
        if self.ids.password_register.background_color != (1, 1, 1, 1):
            self.ids.password_register.background_color = (1, 1, 1, 1)
        if self.ids.password_confirm_register.background_color != (1, 1, 1, 1):
            self.ids.password_confirm_register.background_color = (1, 1, 1, 1)
        if self.ids.email_register.background_color != (1, 1, 1, 1):
            self.ids.email_register.background_color = (1, 1, 1, 1)

class JanelaMain(Screen):
    def on_pre_enter(self):
        center_window(1024, 600)


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('Resources/janelas.kv')  # "Chamar" o arquivo kivy
# (Obs: Se tiver mais de uma janela é preciso declarar essa variável antes do windowManager)


class MoreLife(App):
    def build(self):
        return kv


if __name__ == '__main__':
    MoreLife().run()
