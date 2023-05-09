from threading import Thread
from threading import Event
from time import sleep

class MLTimer:
    horas = 0
    minutos = 0
    lbl_timer = None
    event = None
    
    def __init__(self, hrs1, min1, lbl_tempo):
        self.horas = int(str(hrs1.text))
        self.minutos = int(str(min1.text))
        self.lbl_timer = lbl_tempo
        self.segundos = self.horas*3600 + self.minutos*60
        self.event = Event()

    def iniciar_timer(self):
        b = Thread(target=self.func_timer)
        b.start()

    def fecharThreadTimer(self):
        self.event.set()

    def formatarTimer(self, z):
        formatacao_timer = ""
        if (self.horas < 10):
            formatacao_timer += f"0{self.horas}:"
        else:
            formatacao_timer += f"{self.horas}:"
        if (self.minutos < 10):
            formatacao_timer += f"0{self.minutos}:"
        else:
            formatacao_timer += f"{self.minutos}:"
        if (z%60 < 10):
            formatacao_timer += f"0{z%60}"
        else:
            formatacao_timer += f"{z%60}"
        return formatacao_timer

    def func_timer(self):
        for z in range(self.segundos, -1, -1):
            sleep(1)
            if (self.event.is_set()):
                break
            if(z%60 == 59):
                self.minutos -= 1
            if(self.minutos == -1):
                self.horas -= 1
                self.minutos = int(59)
            self.lbl_timer.text = self.formatarTimer(z)
            print(self.horas, self.minutos, z)

        
        
