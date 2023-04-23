from sys import platform

colors_teme = {'Dark Blue': (0, 0, 70/255, 1), 'Light': (1, 1, 1, 1), 'Dark': (0, 0, 0, 1)}


class WindowInformation:
    @staticmethod
    def get_window_size():
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
            screen_x = GetSystemMetrics(0)
            screen_y = GetSystemMetrics(1)
        else:
            # For mobile devices, use full screen
            screen_x, screen_y = 800, 600  # return something
        return screen_x, screen_y

    @staticmethod
    def center_window(size_x_kivy_window, size_y_kivy_window, window_kivy_instance, size_x_monitor, size_y_monitor):
        window_kivy_instance.size = (size_x_kivy_window, size_y_kivy_window)
        window_kivy_instance.left = (size_x_monitor - size_x_kivy_window) / 2
        window_kivy_instance.top = (size_y_monitor - size_y_kivy_window) / 2


class LoadConfigStuffs:

    def __init__(self, window_kivy_instance, config_list):
        self.window_kivy_instance = window_kivy_instance
        self.config_list = config_list

    def load_main_screen_config(self):
        screen_size = self.config_list[0][1]
        screen_size_w, screen_size_h = screen_size.split(", ")
        self.window_kivy_instance.clearcolor = colors_teme[self.config_list[0][2]]
        return int(screen_size_w), int(screen_size_h)

    def load_text_config(self, resolucao_tela, tema):
        resolucao_tela.text = self.config_list[0][1]
        tema.text = self.config_list[0][2]

    def load_config_color_change(self, teme_name):
        self.window_kivy_instance.clearcolor = colors_teme[teme_name]

    @staticmethod
    def justfy_resolutions_on_screen_config(monitor_size_x, monitor_size_y):
        resolutions = ['FullScreen', '1920, 1440', '2538, 1080', '2436, 1125', '2520, 1080', '1920, 1400', '2048, 1280',
                       '2160, 1200', '2880, 900', '1800, 1440', '2400, 1080', '1856, 1392', '2340, 1080', '1920, 1280',
                       '1920, 1280', '1792, 1344', '2048, 1152', '1920, 1200', '1920, 1280', '1440, 1440', '1920, 1080',
                       '1600, 1280', '1600, 1200', '1776, 1000', '1680, 1050', '1600, 1024', '1440, 1080', '1440, 1024',
                       '1400, 1050', '1600, 900', '1440, 960', '1280, 1024', '1440, 900', '1080, 1200', '1600, 768',
                       '1280, 960', '1280, 854', '1366, 768', '1024, 1024', '1152, 900', '1280, 800', '1334, 750',
                       '1152, 864', '1280, 768', '1120, 832', '1280, 720', '1152, 768', '1152, 720', '1024, 800',
                       '1024, 768', '1138, 640', '1136, 640', '960, 720', '1024, 640', '1024, 600', '960, 640',
                       '1024, 576',
                       '960, 544', '832, 624', '960, 540', '800, 600']
        verif_resu = 1
        while True:
            try:
                w, h = resolutions[verif_resu].split(', ')
                if int(w) >= monitor_size_x or int(h) >= monitor_size_y:
                    resolutions.remove(resolutions[verif_resu])
                else:
                    verif_resu += 1
            except:
                break

        return resolutions

