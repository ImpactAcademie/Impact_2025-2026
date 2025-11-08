from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class HBoxLayout(App):
    def build(self):
        layout = BoxLayout(padding=10)
        for i in range(5):
            layout.add_widget(Button(text="Button", background_color=[1, 0, 0, 1]))
        return layout
class Calculator(App):
    def build(self):
        textinput = TextInput()

        grid = GridLayout(cols=4)
        values = ["7", "8", "9", "+","4", "5", "6", "*", "1", "2", "3", "-", "c", "0", "=", "/"]
        def add_value(instance):
            if instance.text == "c":
                textinput.text = ""
            elif instance.text == "=":
                textinput.text = str(eval(textinput.text))
            else:
                textinput.text +=  instance.text
        for v in values: 
            button = Button(text=v, font_size=50, color=(0.3, 1, 0.5), background_color=(1, 0.3, 1, 0.2))
            button.bind(on_press=add_value)
            grid.add_widget(button)

        

        layout = BoxLayout(orientation="vertical")
        layout.add_widget(textinput)
        layout.add_widget(grid)
        
        return layout

app = Calculator()
app.run()