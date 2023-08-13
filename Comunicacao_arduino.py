from threading import Event
from threading import Thread
import serial
import serial.tools.list_ports


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
            text = self.serialArd.readline()
            btm = int(text.decode('utf'))
            self.ans = str(btm)
            self.lbl_kivy.text = str(self.ans)
            self.MonitorarBTM(btm)

    def MonitorarBTM(self, btm):
        if btm > 100:
            self.user_state.text = "Perigo"
            self.event.clear()
            self.tgb_start_read_beats.state = "normal"
            import simpleaudio as sa
            wave_object = sa.WaveObject.from_wave_file('alert.wav')
            play_object = wave_object.play()
            play_object.wait_done()
            import win32api
            import win32con
            win32api.MessageBox(0, 'Seus batimentos estão acima de 170, notificações foram emviadas para as pessoas'
                                   ' cadastradas', 'BTM Acima de 170!', win32con.MB_ICONEXCLAMATION)
        elif btm > 90:
            self.user_state.text = "Batimentos acima do normal"
        return False
