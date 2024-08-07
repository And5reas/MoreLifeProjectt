import webbrowser
import LoadProgramStuffs as LoadStuff
import DataBase
import MoreLifeTimer as Timer
import Login

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.core.window import Window
from Relatorios import Reports

# Declarando variáveis e objetos
Wi = LoadStuff.WindowInformation()
DBML = DataBase.dataBase()
DBML.createJson()
LoadConfigs = LoadStuff.LoadConfigStuffs(Window, DBML.loadConfig())
Login = Login.confirmLogin()
colorThemeGlobal = (1, 1, 1, 1)


# Dedinir janelas
class JanelaLogin(Screen):
    checar = True

    def btn_registrar(self):
        webbrowser.open("https://morelife.vercel.app/")

    def btn_login(self):
        user_email = self.ids.email_input.text
        user_password = self.ids.password_input.text

        if Login.Check(user_email, user_password, DBML):
            self.ids.error_login.text = ""
            if self.ids.check_keep_login.active:
                DBML.saveConfig('isLogged', 1)
            else:
                DBML.saveConfig('isLogged', 0)
            return True
        else:
            self.ids.password_input.background_color = (212 / 255, 25 / 255, 32 / 255, .6)
            self.ids.email_input.background_color = (212 / 255, 25 / 255, 32 / 255, .6)
            self.ids.error_login.text = "Email e/ou senha inválido(s)"
        return False

    def validate_color(self):
        if self.ids.password_input.background_color != (1, 1, 1, 1):
            self.ids.password_input.background_color = (1, 1, 1, 1)
        if self.ids.email_input.background_color != (1, 1, 1, 1):
            self.ids.email_input.background_color = (1, 1, 1, 1)

    def remove_password_mask(self):
        if not self.checar:
            self.checar = True
            self.ids.eye_password_mask.source = "Resources/Imgs/zoio_fechado.png"
        else:
            self.checar = False
            self.ids.eye_password_mask.source = "Resources/Imgs/zoio_aberto.png"
        self.ids.password_input.password = self.checar

    def keep_login(self, radio_button):
        if radio_button:
            self.ids.check_keep_login.active = False
        else:
            self.ids.check_keep_login.active = True

    def on_kv_post(self, base_widget):
        if LoadConfigs.IsLogged == 1:
            saved_screen_size_w, saved_screen_size_h = LoadConfigs.load_main_screen_config()
            Wi.center_window(saved_screen_size_w, saved_screen_size_h, Window)
            self.manager.current = 'main_screen'
        saved_screen_size_w, saved_screen_size_h = LoadConfigs.load_main_screen_config()
        Wi.center_window(saved_screen_size_w, saved_screen_size_h, Window)
        LoadConfigs.load_config_color_change("Dark")


class JanelaMain(Screen):
    def start_read_beats(self):
        from Comunicacao_arduino import Reading
        global ard_comunic_thread
        if ard_comunic_thread is None:
            ard_comunic_thread = Reading()
        if self.ids.tgb_start_read_beats.state == 'down':
            ard_comunic_thread.event.set()
            ard_comunic_thread.iniciar(self.ids.Batimentos, self.ids.tgb_start_read_beats, self.ids.user_state,
                                       self.ids.tgb_start_read_beats)
            self.ids.tgb_start_read_beats.text = 'Parar'
        if self.ids.tgb_start_read_beats.state == 'normal':
            ard_comunic_thread.event.clear()
            self.ids.tgb_start_read_beats.text = 'Começar'

    def on_pre_enter(self, *args):
        self.colorTheme = colorThemeGlobal
        return super().on_pre_enter(*args)


class POPUP(Popup):
    lbl_nome_timer = None
    lbl_timer = None
    class_timer_name = None

    def validar_timer(self):
        validar = [self.ids.Spn_hrs.text, self.ids.Spn_min.text, self.ids.Spn_sec.text]
        oq_validar = ["Horas", "Minutos", "Segundos"]
        j = 0
        r = []
        for i in validar:
            if i == oq_validar[j]:
                r.append('00')
            else:
                r.append(i)
            j += 1

        nome = self.ids.TxtInp_mudarNome.text
        if nome == "NOME" or nome == "":
            r.append("------------")
        else:
            r.append(nome)
        return r

    def extanciar_layout(self, lbl_nome_timer, lbl_timer, class_timer):
        self.lbl_timer = lbl_timer
        self.lbl_nome_timer = lbl_nome_timer
        self.class_timer_name = class_timer.name

    def modificar(self):
        horas, minutos, segundos, nome = self.validar_timer()
        DBML.saveConfig(self.class_timer_name, f"{horas}:{minutos}:{segundos};{nome}")
        LoadConfigs.update_dados(DBML.loadConfig())
        if self.class_timer_name == "Timer1":
            self.lbl_timer.text, self.lbl_nome_timer.text = LoadConfigs.timers[0].split(';')
        if self.class_timer_name == "Timer2":
            self.lbl_timer.text, self.lbl_nome_timer.text = LoadConfigs.timers[1].split(';')
        if self.class_timer_name == "Timer3":
            self.lbl_timer.text, self.lbl_nome_timer.text = LoadConfigs.timers[2].split(';')
        if self.class_timer_name == "Timer4":
            self.lbl_timer.text, self.lbl_nome_timer.text = LoadConfigs.timers[3].split(';')
        self.dismiss()


class TIMER(BoxLayout):
    checar = False

    def set_img_pause(self):
        self.ids['imgPlay'].source = "Resources/Imgs/Pause.png"
        self.checar = True

    def set_img_start(self):
        self.ids['imgPlay'].source = "Resources/Imgs/Play.png"
        self.checar = False

    def load_timer(self, name):
        if name == "Timer1":
            self.ids.lbl_timer_timer.text, self.ids.lbl_nome_timer.text = LoadConfigs.timers[0].split(';')
        elif name == "Timer2":
            self.ids.lbl_timer_timer.text, self.ids.lbl_nome_timer.text = LoadConfigs.timers[1].split(';')
        elif name == "Timer3":
            self.ids.lbl_timer_timer.text, self.ids.lbl_nome_timer.text = LoadConfigs.timers[2].split(';')
        elif name == "Timer4":
            self.ids.lbl_timer_timer.text, self.ids.lbl_nome_timer.text = LoadConfigs.timers[3].split(';')

    def on_kv_post(self, base_widget):
        self.load_timer(self.name)

    @staticmethod
    def kill_chrono(name):
        if name == "Timer1":
            temporizador1.fecharThreadTimer()
        elif name == "Timer2":
            temporizador2.fecharThreadTimer()
        elif name == "Timer3":
            temporizador3.fecharThreadTimer()
        elif name == "Timer4":
            temporizador4.fecharThreadTimer()

    def add_chrono(self, lbl_tempo, name):
        hrs, minn, sec = lbl_tempo.text.split(':')
        if name == "Timer1":
            temporizador1.iniciar_timer(hrs, minn, sec, lbl_tempo, self.ids['imgPlay'])
        elif name == "Timer2":
            temporizador2.iniciar_timer(hrs, minn, sec, lbl_tempo, self.ids['imgPlay'])
        elif name == "Timer3":
            temporizador3.iniciar_timer(hrs, minn, sec, lbl_tempo, self.ids['imgPlay'])
        elif name == "Timer4":
            temporizador4.iniciar_timer(hrs, minn, sec, lbl_tempo, self.ids['imgPlay'])

    def play_pause(self, lbl_tempo):
        if not self.checar:
            self.set_img_pause()
            self.add_chrono(lbl_tempo, self.name)
        else:
            self.set_img_start()
            self.kill_chrono(self.name)

    def editar(self, class_timer):
        popup = POPUP()
        popup.extanciar_layout(self.ids.lbl_nome_timer, self.ids.lbl_timer_timer, class_timer)
        popup.open()

    def resetar(self):
        self.set_img_start()
        self.load_timer(self.name)
        self.kill_chrono(self.name)


class JanelaAlertas(Screen):
    def on_pre_enter(self, *args):
        self.colorTheme = colorThemeGlobal
        return super().on_pre_enter(*args)


class JanelaReport(Screen, Reports):

    def on_pre_enter(self):
        self.colorTheme = colorThemeGlobal
    
    def gerar_relatorio(self):
        # Reports.clickkbutton(self)
        try:
            Reports.bl = ard_comunic_thread.btmList
            Reports.d = ard_comunic_thread.diff
            Reports.create_image(self)
        except:
            pass


class JanelaConfig(Screen):
    @staticmethod
    def change_tema(tema):
        global colorThemeGlobal
        if tema == "White":
            colorThemeGlobal = (0, 0, 0, 1)
        else:
            colorThemeGlobal = (1, 1, 1, 1)
        LoadConfigs.load_config_color_change(tema)
        DBML.saveConfig('theme', tema)


class WindowManager(ScreenManager):
    def deslogar(self):
        DBML.saveConfig('isLogged', 0)
        self.current = "login_screen"


class MoreLife(App):
    def build(self):
        from kivy.config import Config
        Config.read("morelife.ini")
        self.icon = "Resources/Imgs/icon.png"
        return kv

    def on_stop(self):
        if ard_comunic_thread is not None:
            ard_comunic_thread.event.clear()
        temp_list = [temporizador1, temporizador2, temporizador3, temporizador4]
        for i in temp_list:
            if i is not None:
                i.fecharThreadTimer()


kv = Builder.load_file('Resources/janelas.kv')  # "Chamar" o arquivo kivy
# (Obs: Se tiver mais de uma janela é preciso declarar essa variável antes do windowManager)

ard_comunic_thread = None
temporizador1 = Timer.MLTimer()
temporizador2 = Timer.MLTimer()
temporizador3 = Timer.MLTimer()
temporizador4 = Timer.MLTimer()
