import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


def press(name, pizza, color, grid):
    # Print at terminal
    # print(f'Hello {name}, you like {pizza} pizza, and you favorite color is {color}! :)')

    # Print it to the Screen
    grid.add_widget(Label(text=f'Hello {name.text}, you like {pizza.text} pizza, and you favorite color is '
                               f'{color.text}! :)'))

    name.text = ''
    pizza.text = ''
    color.text = ''


class MyApp(App):
    def build(self):
        buttons_grid = GridLayout(cols=1,
                                  row_force_default=True,
                                  row_default_height=120,
                                  col_force_default=True,
                                  col_default_width=100)

        text_input_grid = GridLayout(cols=2,
                                     row_force_default=True,
                                     row_default_height=40,
                                     col_force_default=True,
                                     col_default_width=100)

        # Add widgets
        text_input_grid.add_widget(Label(text="Name: "))
        name = TextInput(multiline=False)
        text_input_grid.add_widget(name)

        text_input_grid.add_widget(Label(text="Favorite pizza: "))
        pizza = TextInput(multiline=False)
        text_input_grid.add_widget(pizza)

        text_input_grid.add_widget(Label(text="Favorite color: "))
        color = TextInput(multiline=False)
        text_input_grid.add_widget(color)

        buttons_grid.add_widget(text_input_grid)

        # Create a Submit Button
        submit = Button(text="Submit", font_size="30",
                        size_hint_y=None, height=40,
                        size_hint_x=None, width=200)
        # Bind the button
        submit.bind(on_press=lambda x: press(name, pizza, color, buttons_grid))

        buttons_grid.add_widget(submit)

        return buttons_grid


if __name__ == '__main__':
    MyApp().run()
