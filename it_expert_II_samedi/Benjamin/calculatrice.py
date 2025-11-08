from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

entry = ""

class Calculator(App):
    def build(self):
        label = TextInput(text="", size_hint=(1, 0.5))
        grid = GridLayout(cols=4, padding=10, spacing=10)
        buttonList = ("7","8","9","+","4","5","6","-","1","2","3","*","C","0","=","/")
        for i in range(16):
            def callback(instance):    
                if instance.text == "C":
                    label.text = ""
                elif instance.text == "=" and label.text[-1] in ["+","-","*","/"]:
                    return
                elif instance.text == "=":
                    label.text = str(eval(label.text))
                elif instance.text in ["+","-","*","/"] and label.text[-1] in ["+","-","*","/"]:
                    return
                else:
                    label.text += instance.text
            button = Button(text=buttonList[i], font_size=30)
            button.bind(on_press=callback)
            grid.add_widget(button)
        box = BoxLayout(orientation="vertical")
        box.add_widget(label)
        box.add_widget(grid)
        return box
if __name__ == "__main__":
    calc = Calculator()
    calc.run()
