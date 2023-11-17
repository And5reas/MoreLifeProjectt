import matplotlib.pyplot as plt
# import numpy as np
import datetime
# from threading import Thread
from Comunicacao_arduino import Reading

class Reports(Reading):
    bl = []
    d = []

    # texto = " "

    # def clickkbutton(self):
    #     b = Thread(target=self.create_image)
    #     b.start()

    # def variables(self, texto):
    #     self.texto = texto

    # def create_report(self):
    #     self.Wfile = open('relatorios.txt', 'w')
    #     for i in range(0, len(self.btmList)):
    #         self.texto = f"""{self.btmList[i]},{self.difference} \n"""
    #         self.Wfile.write(self.texto)
    #     self.open_file()

    # def open_file(self):
    #     self.file = open('relatorios.txt', 'r')
    #     self.linha = self.file.readlines()
    #     self.report_handle()

    # def findValue(self):
    #     self.fullstring = self.fullstring.rstrip('\n')
    #     self.value = self.fullstring[:self.fullstring.index(' , ')]
    #     return self.value

    # def report_handle(self):
    #     for linha in self.linha:
    #         if(len(linha) == 0):
    #             self.msg = "Não há valores encontrados para gerar relatórios..."
    #             self.ids.lbl_msg.text = self.msg
    #         else:
    #             self.create_image()

    def create_image(self):
        # self.dateNow = datetime.datetime.now()
        # self.data = np.loadtxt('relatorios.txt', delimiter=',')
        # for i in range(len(self.data)):
        #     for j in range(2):
        #         if j == 0:
        #             self.x.append(self.data[i][j])
        #         else:
        #             self.y.append(self.data[i][j])
        try:
            if(len(self.bl) > 0):
                self.aux = self.bl
                plt.plot(self.d, self.bl)
                plt.title('Relatório gerado')
                plt.xlabel('Tempo corrido(segundos)')
                plt.ylabel('BPM(Batimentos por minuto)')
                plt.show()
            # plt.savefig("Relatorios/relatorio_" + self.dateNow.strftime("%y-%m-%d %H:%M:%S") + ".png")
            else:
                self.msg = "Não há valores encontrados para gerar relatórios..."
                import win32api
                import win32con
                win32api.MessageBox(0, self.msg, "Erro...", win32con.MB_ICONEXCLAMATION)

        except:
            pass

