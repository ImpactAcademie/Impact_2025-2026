from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.lang.builder import Builder
class Calculator(App):
    def build(self):
        grid = GridLayout(cols=4)
        for i in range(16):
             grid.add_widget(Button(text="Cliquez moi", font_size=20))
        return grid
        # return Builder.load_file("calculatrice.kv")
    
calc = Calculator()
calc.run()