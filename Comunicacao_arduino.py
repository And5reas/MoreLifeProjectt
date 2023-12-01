from threading import Event
from threading import Thread
import serial
import serial.tools.list_ports
import requests
from DataBase import dataBase
from datetime import datetime
from twilio.rest import Client
from time import sleep

class Reading:
    serialArd = serial.Serial()
    event = Event()

    funciona = False
    option = None
    ans = None
    lbl_kivy = None
    tgb_kivy = None
    ports = None
    user_state = None
    tgb_start_read_beats = None
    btmList = []
    difference = 0
    diff = []
    start = 0
    end = 0
    phoneNunber = None

    def iniciar(self, lbl_kivy, tgb_kivy, user_state, tgb_start_read_beats):
        self.ports = serial.tools.list_ports.comports()
        self.serialArd.close()
        a = Thread(target=self.connect)
        self.lbl_kivy = lbl_kivy
        self.tgb_kivy = tgb_kivy
        self.user_state = user_state
        self.tgb_start_read_beats = tgb_start_read_beats
        a.start()

    @staticmethod
    def verificar_portas_com(porta):
        lista = ["Porta de comunicação", "Communications Port"]
        for i in lista:
            if porta == i:
                return False
        return True

    def connect(self):
        try:
            for port in self.ports:
                port = str(port)
                porta, name_porta = port.split(' - ')
                name_porta = name_porta.split(' (')
                if self.verificar_portas_com(name_porta[0]):
                    self.option = porta
                    self.funciona = True
                    break
        except:
            pass
        if self.funciona:
            self.readArd()
        else:
            self.tgb_kivy.state = 'normal'
            self.tgb_kivy.text = 'Começar'
            self.lbl_kivy.text = 'Não foi possível conectar ao MoreLife'

    def readArd(self):
        self.serialArd.close()
        self.serialArd.baudrate = 115200
        self.serialArd.port = self.option
        self.serialArd.open()
        self.readingSerialArd()

    def readingSerialArd(self):
        while self.event.is_set():
            self.start = datetime.now().minute
            text = self.serialArd.readline()
            try:
                btm = int(text.decode('utf'))
            except:
                pass
            self.ans = str(btm)
            self.lbl_kivy.text = str(self.ans)
            if (self.start != self.end):
                self.btmList.append(btm)
                self.diff.append(f'{datetime.now().hour}:{self.start}')
            self.mediabtm = sum(self.btmList)/len(self.btmList)
            self.MonitorarBTM(btm)
            self.end = datetime.now().minute
            sleep(0.05)

    def MonitorarBTM(self, btm):
        if btm > 100:
            self.event.clear()
            self.tgb_start_read_beats.state = "normal"
            requisicao = requests.get("https://morelife-f4ffa-default-rtdb.firebaseio.com/tb_responsavel/.json")
            tb_responsavel = requisicao.json()

            for id_responsavel in tb_responsavel:
                id_user = tb_responsavel[id_responsavel]['id_user']
                if id_user == dataBase.getsaveUser():
                    self.phoneNunber = F"+55{tb_responsavel[id_responsavel]['nb_cell']}"

            self.user_state.text = "Perigo"

            client = Client('AC6f856637664320539b3980367adcaad5', '22b6ba485fe31baab4157bafe8b72147')

            client.messages.create(from_='+14437207354',
                        to=self.phoneNunber,
                        body=F'MoreLife: O usuário está em perigo')
        elif btm > 90:
            self.user_state.text = "Batimentos acima do normal"
        return True # Voltar para FALSE
        
