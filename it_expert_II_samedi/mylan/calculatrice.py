from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

entry =""

class Calculator(App):
    def build(self):
        label = Label(text=entry)

        grid = GridLayout(cols=4)
        texts = ["7", "8", "9", "+", "4", "5", "6", "-", "1", "2", "3", "*", "C", "0", "=", "/"]
        for i in range(16):
            def callback(instance):
                global entry
                entry += texts[i]
            button = Button(text=texts[i], font_size=60)
            button.bind(on_press=callback)
            grid.add_widget(button)
        box = BoxLayout(orientation="vertical")
        box.add_widget(label)
        box.add_widget(grid)
        return box
            
        return grid
        return Builder.load_file("calculatrice.kv")
    
calc = Calculator()
calc.run()