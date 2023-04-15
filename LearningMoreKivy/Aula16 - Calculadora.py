from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

# Set the app size
Window.size = (500, 700)

# Point de .kv file
Builder.load_file('KV files/calculadora.kv')


class MyLayout(Widget):
    def btn_clear(self):
        self.ids.calc_input.text = "0"

    # Create a button pressing function
    def btn_press(self, number):
        prior = self.ids.calc_input.text

        if prior == "0":
            self.ids.calc_input.text = ''
            self.ids.calc_input.text += f"{number}"
        else:
            self.ids.calc_input.text += f"{number}"

    def math_sings(self, sing):
        prior = self.ids.calc_input.text

        bool_print = True

        list_sings = ['+', '-', '*', '/']
        for i in list_sings:
            if prior[-1] == i:
                bool_print = False

        if bool_print:
            self.ids.calc_input.text += sing
        else:
            self.ids.calc_input.text = f"{prior[:-1]}{sing}"

    def btn_calc(self):
        prior = self.ids.calc_input.text

        # Fazer as outras operações depois
        if "+" in prior:
            num_list = prior.split("+")
            answer = 0
            for number in num_list:
                answer += int(number)
            self.ids.calc_input.text = str(answer)


class CalculatorApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    CalculatorApp().run()
