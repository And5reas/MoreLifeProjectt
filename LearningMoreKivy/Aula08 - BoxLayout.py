from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file('KV files/label_color.kv')


class MyLayout(Widget):
    pass


class AwsomeApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    AwsomeApp().run()
