from sys import platform


class WindowInformation:
    size_x_monitor = None
    size_y_monitor = None

    def __init__(self):
        self.get_window_size()

    def get_window_size(self):
        # Checar qual o tamanho do monitor do usuário
        if platform == 'linux2':
            import subprocess
            output = subprocess.Popen(
                'xrandr | grep "\*" | cut -d" " -f4',
                shell=True,
                stdout=subprocess.PIPE).communicate()[0]
            screen_x = int(output.replace('\n', '').split('x')[0])
            screen_y = int(output.replace('\n', '').split('x')[1])
        elif platform == 'win32':
            from win32api import GetSystemMetrics
            import ctypes
            screen_x = GetSystemMetrics(0)
            screen_y = GetSystemMetrics(1)
            ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
        else:
            # For mobile devices, use full screen
            screen_x, screen_y = 800, 600  # return something
        self.size_x_monitor = screen_x
        self.size_y_monitor = screen_y

    def center_window(self, size_x_kivy_window, size_y_kivy_window, window_kivy_instance):
        window_kivy_instance.size = (size_x_kivy_window, size_y_kivy_window)
        window_kivy_instance.left = (self.size_x_monitor - size_x_kivy_window) / 2
        window_kivy_instance.top = (self.size_y_monitor - size_y_kivy_window) / 2


class LoadConfigStuffs:
    config_list = ""
    IsLogged = 0
    timers = []

    def __init__(self, window_kivy_instance, config_list):
        self.window_kivy_instance = window_kivy_instance
        self.update_dados(config_list)
        self.colors_teme = {'Dark Blue': (0, 0, 70/255, 1), 'Dark': (0, 0, 0, 1)}

    def update_dados(self, lista):
        self.config_list = lista
        self.IsLogged = lista['isLogged']
        self.timers = [lista['Timer1'], lista['Timer2'], lista['Timer3'], lista['Timer4']]

    def load_main_screen_config(self):
        screen_size = self.config_list['resolution']
        screen_size_w, screen_size_h = screen_size.split(", ")
        self.window_kivy_instance.clearcolor = self.colors_teme[self.config_list['theme']]
        return int(screen_size_w), int(screen_size_h)

    def load_config_color_change(self, teme_name):
        self.window_kivy_instance.clearcolor = self.colors_teme[teme_name]
