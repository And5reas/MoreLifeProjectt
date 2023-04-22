from kivy.config import Config
Config.set('graphics', 'resizable', 0)
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

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

        if user_email == "1" and user_password == "123":
            center_window(*tamanho_tela)
            return True

        if "@" in user_email:
            self.ids.error_login.text = ""
            nome_user_email, domain_email = user_email.split("@")
            print(f"Nome do email: {nome_user_email}\nServidor: {domain_email}")
            print(f"Email: {user_email}\nSenha: {user_password}")
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
        Window.clearcolor = (1, 1, 1, 1)

    def remove_password_mask(self):
        if not self.checar:
            self.checar = True
            self.ids.eye_password_mask.source = "Resources\Imgs\ZoioFechado.png"
        else:
            self.checar = False
            self.ids.eye_password_mask.source = "Resources\Imgs\ZoioAberto.png"
        self.ids.password_input.password = self.checar

    def keep_login(self, radio_button):
        if radio_button:
            self.ids.check_keep_login.active = False
        else:
            self.ids.check_keep_login.active = True


class JanelaMain(Screen):
    def on_pre_enter(self):
        pass


class JanelaReport(Screen):
    def on_pre_enter(self):
        pass


class JanelaConfig(Screen):
    def change_tema(self, tema):
        if tema == "Dark":
            Window.clearcolor = (0, 0, 0, 1)
        if tema == "Light":
            Window.clearcolor = (1, 1, 1, 1)

    def change_resolution(self, resolution):
        if resolution == "FullScreen":
            center_window(screen_x, screen_y)
        else:
            h, w = resolution.split(',')
            center_window(int(h), int(w))

    def on_pre_enter(self):
        self.ids.resolucao_config.values = resolutions


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('Resources/janelas.kv')  # "Chamar" o arquivo kivy
# (Obs: Se tiver mais de uma janela é preciso declarar essa variável antes do windowManager)

tamanho_tela = (1024, 600)
resolutions = ['FullScreen', '1920, 1440', '2538, 1080', '2436, 1125', '2520, 1080', '1920, 1400', '2048, 1280',
               '2160, 1200', '2880, 900', '1800, 1440', '2400, 1080', '1856, 1392', '2340, 1080', '1920, 1280',
               '1920, 1280', '1792, 1344', '2048, 1152', '1920, 1200', '1920, 1280', '1440, 1440', '1920, 1080',
               '1600, 1280', '1600, 1200', '1776, 1000', '1680, 1050', '1600, 1024', '1440, 1080', '1440, 1024',
               '1400, 1050', '1600, 900', '1440, 960', '1280, 1024', '1440, 900', '1080, 1200', '1600, 768',
               '1280, 960', '1280, 854', '1366, 768', '1024, 1024', '1152, 900', '1280, 800', '1334, 750',
               '1152, 864', '1280, 768', '1120, 832', '1280, 720', '1152, 768', '1152, 720', '1024, 800',
               '1024, 768', '1138, 640', '1136, 640', '960, 720', '1024, 640', '1024, 600', '960, 640', '1024, 576',
               '960, 544', '832, 624', '960, 540', '800, 600']
verif_resu = 1
while True:
    try:
        w, h = resolutions[verif_resu].split(', ')
        if int(w) >= screen_x or int(h) >= screen_y:
            resolutions.remove(resolutions[verif_resu])
        else:
            verif_resu += 1
    except:
        break


class MoreLife(App):
    def build(self):
        self.icon = "Resources/Imgs/icon.png"
        return kv


if __name__ == '__main__':
    MoreLife().run()
