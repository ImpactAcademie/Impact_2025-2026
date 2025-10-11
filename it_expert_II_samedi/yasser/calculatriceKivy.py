from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

entry = ""

class Calculator(App):
    def build(self):
        label = Label(text=entry)
        grid = GridLayout(cols=4, padding=10, spacing=10)
        buttonList = ("7","8","9","+","4","5","6","-","1","2","3","*","C","0","=","/")
        for i in range(16):
            def callback(instance):
                global entry
                entry += buttonList[i]
            button = Button(text=buttonList[i], font_size=30)
            button.bind(on_press=callback)
            grid.add_widget(button)
        box = BoxLayout(orientation="vertical")
        box.add_widget(label)
        box.add_widget(grid)
        return box

calc = Calculator()
calc.run()
