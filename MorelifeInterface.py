import LoadProgramStuffs as LoadStuff
import DataBaseMorelife as DBMorelife
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
# Isso precisa estar antes do "from kivy.core.window import Window" se não um sobrepõe o outro
from kivy.config import Config
Config.set('graphics', 'resizable', 0)
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

from kivy.core.window import Window


# Dedinir janelas
class JanelaLogin(Screen):
    checar = True

    def btn_login(self):
        user_email = self.ids.email_input.text
        user_password = self.ids.password_input.text

        if user_email == "1" and user_password == "123":
            saved_screen_size_w, saved_screen_size_h = LoadConfigs.load_main_screen_config()
            Wi.center_window(saved_screen_size_w, saved_screen_size_h, Window, screen_x, screen_y)
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
        Wi.center_window(420, 350, Window, screen_x, screen_y)
        Window.clearcolor = (1, 1, 1, 1)

    def remove_password_mask(self):
        if not self.checar:
            self.checar = True
            self.ids.eye_password_mask.source = "Resources\\Imgs\\zoio_fechado.png"
        else:
            self.checar = False
            self.ids.eye_password_mask.source = "Resources\\Imgs\\zoio_aberto.png"
        self.ids.password_input.password = self.checar

    def keep_login(self, radio_button):
        if radio_button:
            self.ids.check_keep_login.active = False
        else:
            self.ids.check_keep_login.active = True


class JanelaAlertas(Screen):
    pass


class JanelaMain(Screen):
    def on_pre_enter(self):
        pass

    def start_read_beats(self):
        from Comunicacao_arduino import Reading
        global ard_comunic_thread
        ard_comunic_thread = Reading()
        if self.ids.tgb_start_read_beats.state == 'down':
            ard_comunic_thread.event.set()
            ard_comunic_thread.iniciar(self.ids.Batimentos)
            self.ids.tgb_start_read_beats.text = 'Parar'
        if self.ids.tgb_start_read_beats.state == 'normal':
            ard_comunic_thread.event.clear()
            self.ids.tgb_start_read_beats.text = 'Começar'


class JanelaReport(Screen):
    def on_pre_enter(self):
        pass


class JanelaConfig(Screen):
    @staticmethod
    def change_tema(tema):
        LoadConfigs.load_config_color_change(tema)
        DBConfig.save_config('Teme', tema)

    @staticmethod
    def change_resolution(resolution):
        if resolution == "FullScreen":
            Wi.center_window(screen_x, screen_y, Window, screen_x, screen_y)
        else:
            h, w = resolution.split(',')
            Wi.center_window(int(h), int(w), Window, screen_x, screen_y)
        DBConfig.save_config('Resolution', resolution)

    def on_leave(self):
        DBConfig.commit_and_close()

    def on_pre_enter(self):
        self.ids.resolucao_config.values = resolutions
        DBConfig.start_connection()


class WindowManager(ScreenManager):
    pass


class MoreLife(App):
    def build(self):
        self.icon = "Resources/Imgs/icon.png"
        return kv

    def on_stop(self):
        ard_comunic_thread.event.clear()


# Declarando variáveis e objetos
Wi = LoadStuff.WindowInformation()
screen_x, screen_y = Wi.get_window_size()
kv = Builder.load_file('Resources/janelas.kv')  # "Chamar" o arquivo kivy
# (Obs: Se tiver mais de uma janela é preciso declarar essa variável antes do windowManager)
DBConfig = DBMorelife.ConfigDataBase()
DBConfig.create_db()
LoadConfigs = LoadStuff.LoadConfigStuffs(Window, DBConfig.load_config())
resolutions = LoadConfigs.justfy_resolutions_on_screen_config(screen_x, screen_y)

ard_comunic_thread = None
