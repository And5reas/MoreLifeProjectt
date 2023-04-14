from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.config import Config

Builder.load_file('Resources/Janelas/login.kv')  # "Chamar" o arquivo kivy
Config.set('graphics', 'resizable', '0')  # Configurar a janela para não poder ser redimensionada
Config.set('graphics', 'width', '420')  # "Setar" a largura da janela
Config.set('graphics', 'height', '350')  # "Setar" a altura da janela


class MyLayout(Widget):
    pass


class Login(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    Login().run()
