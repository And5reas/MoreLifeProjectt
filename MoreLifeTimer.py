from threading import Thread
from threading import Event
from time import sleep
# from winotify import Notification, audio


class MLTimer:
    horas = 0
    minutos = 0
    segundos = 0
    lbl_timer = None
    event = None
    default_timer = None
    timerImage = None
    notificacao = None
    
    def __init__(self):
        self.event = Event()

    def iniciar_timer(self, hrs, minn, sec, lbl_tempo, instance_timer_btnPlay):
        self.horas = int(hrs)
        self.minutos = int(minn)
        self.lbl_timer = lbl_tempo
        self.default_timer = lbl_tempo.text
        self.segundos = self.horas * 3600 + self.minutos * 60 + int(sec)
        self.timerImage = instance_timer_btnPlay
        # self.notificacao = Notification(app_id="MoreLife",
                                        # title="MoreLife Alarme",
                                        # msg="Tempo expirado",
                                        # duration="short")
        # self.notificacao.add_actions(label="Ok")
        # self.notificacao.set_audio(audio.LoopingAlarm, loop=True)
        b = Thread(target=self.func_timer)
        b.start()

    def fecharThreadTimer(self):
        self.event.set()

    def formatarTimer(self, z):
        formatacao_timer = ""
        if self.horas < 10:
            formatacao_timer += f"0{self.horas}:"
        else:
            formatacao_timer += f"{self.horas}:"
        if self.minutos < 10:
            formatacao_timer += f"0{self.minutos}:"
        else:
            formatacao_timer += f"{self.minutos}:"
        if z % 60 < 10:
            formatacao_timer += f"0{z%60}"
        else:
            formatacao_timer += f"{z%60}"
        return formatacao_timer

    def func_timer(self):
        self.event.clear()
        angulo_circulo = 360/self.segundos
        for z in range(self.segundos, -1, -1):
            sleep(1)
            if self.event.is_set():
                break
            if z % 60 == 59:
                self.minutos -= 1
            if self.minutos == -1:
                self.horas -= 1
                self.minutos = int(59)
            self.lbl_timer.text = self.formatarTimer(z)
            self.lbl_timer.animation_ellipse = angulo_circulo * z
        if self.lbl_timer.text == '00:00:00':
            self.notificacao.show()
            self.notificacao = None
            sleep(1)
            self.lbl_timer.animation_ellipse = 360
            self.lbl_timer.text = self.default_timer
            self.timerImage.source = "Resources/Imgs/Play.png"
        self.event.clear()

        
        
