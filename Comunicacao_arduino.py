import serial.tools.list_ports
import serial
from threading import Thread
from threading import Event


class Reading:
    serialArd = serial.Serial()
    event = Event()

    funciona = False
    option = None
    ans = None
    lbl_kivy = None
    tgb_kivy = None
    ports = None

    def iniciar(self, lbl_kivy, tgb_kivy):
        self.ports = serial.tools.list_ports.comports()
        self.serialArd.close()
        a = Thread(target=self.connect)
        self.lbl_kivy = lbl_kivy
        self.tgb_kivy = tgb_kivy
        a.start()

    def connect(self):
        try:
            for port in self.ports:
                port = str(port)
                porta, name_porta = port.split(' - ')
                name_porta = name_porta.split(' (')
                if name_porta[0] == "Arduino Uno":
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
            text = self.serialArd.readline()
            self.ans = str(text.decode('utf'))
            self.lbl_kivy.text = str(self.ans)
