import serial.tools.list_ports
import serial


def connect(ports):
    try:
        for onePort in ports:
            comList.append(str(onePort))
            print(str(onePort))
        print("\nEssas são as portas disponíveis em sua máquina para conectar no Arduino")

    except:
        print("Nenhuma porta para conectar no Arduino...")

    op = int(input("\nDigite o número da porta que está conectada ao Arduino(PODE SER VISTA NA IDE DO ARDUINO): "))
    for x in range(0, len(comList)):
        if(comList[x].startswith("COM" + str(op))):
            option = "COM" + str(op)
            print("Conectado a", option)
            readArd(serialArd, option)
        else:
            print("Não foi possível achar nenhuma porta COM...")
            return connect(ports)


def readArd(serialArd, option):
    serialArd.baudrate = 115200
    serialArd.port = option
    serialArd.open()
    text = serialArd.read(100)
    print(text.decode('utf'))
    op_cl = input("Deseja 'printar' mais resultados do sensor?(Y OU N): ")
    if(op_cl == 'Y'):
        return readArd(serialArd, option)
    elif(op_cl == 'N'):
        serialArd.close()
    else:
        print("Opção não válida...")
        return readArd(serialArd, option)


ports = serial.tools.list_ports.comports()
serialArd = serial.Serial()

comList = []

connect(ports)