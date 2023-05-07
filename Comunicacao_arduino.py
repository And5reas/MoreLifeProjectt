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
                if name_porta[0] != "Porta de comunicação":
                    self.option = porta
                    print("Conectado a", self.option)
                    self.funciona = True
                    break
                else:
                    print(f"Não foi possível achar nenhuma porta {porta}")  # Vai ser removido no futuro
        except:
            print("Nenhuma porta para conectar no Arduino...")  # Vai ser removido no futuro
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
        print("Conexão encerrada!")
