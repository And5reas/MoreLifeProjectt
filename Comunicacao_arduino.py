import serial.tools.list_ports
import serial
from threading import Thread
from threading import Event


class Reading:
    ports = serial.tools.list_ports.comports()
    serialArd = serial.Serial()
    event = Event()

    funciona = False
    option = None
    ans = None
    lbl_kivy = None

    def iniciar(self, lbl_kivy):
        a = Thread(target=self.connect)
        self.lbl_kivy = lbl_kivy
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
            print(self.ans)
            self.lbl_kivy.text = str(self.ans)
        print("Conexão encerrada!")
