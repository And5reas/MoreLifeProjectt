import serial.tools.list_ports
import serial
from threading import Thread

class Reading:

    ports = serial.tools.list_ports.comports()
    serialArd = serial.Serial()

    comList = []

    ans = ''

    def iniciar(self):
        a = Thread(target=self.connect)
        a.start()

    def connect(self):
        try:
            for onePort in self.ports:
                self.comList.append(str(onePort))
                print(str(onePort))
            print("\nEssas são as portas disponíveis em sua máquina para conectar no Arduino")

        except:
            print("Nenhuma porta para conectar no Arduino...")

        # op = int(input("\nDigite o número da porta que está conectada ao Arduino(PODE SER VISTA NA IDE DO ARDUINO): "))
        for x in range(-1, 20):
            print(x)
            try:
                if(self.comList[x].startswith("COM" + str(x))):
                    self.option = "COM" + str(x)
                    print("Conectado a", self.option)
                    self.readArd()
                else:
                    print("Não foi possível achar nenhuma porta COM...")
                    try:
                        for onePort in self.ports:
                            self.comList.append(str(onePort))
                            print(str(onePort))
                        print("\nEssas são as portas disponíveis em sua máquina para conectar no Arduino")

                    except:
                        print("Nenhuma porta para conectar no Arduino...")
            except:
                pass


    def readArd(self):
        self.serialArd.close()
        self.serialArd.baudrate = 115200
        self.serialArd.port = self.option
        self.serialArd.open()
        self.readingSerialArd()


    def readingSerialArd(self):
        i = 0
        while True:
            text = self.serialArd.readline()
            self.ans = str(text.decode('utf'))
            print(self.ans)
            if (i > 10000):
                op_cl = input("Deseja 'printar' mais resultados do sensor?(Y OU N): ")
                while(op_cl.upper() == 'Y'):
                    i = 0
                    self.readArd()
                if(op_cl.upper() == 'N'):
                    return False
                else:
                    print('Digite uma opção válida...')
                    return self.readArd()
            i += 1

