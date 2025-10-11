from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.lang.builder import Builder
class Calc(App):
    def build(self):
        grid = GridLayout(cols=4)
        texts = ["7","8","9","+","4","5","6","-","1","2","3","*","C","0","=","/"]
        for i in range(16):
            grid.add_widget(Button(text="Cliquez moi", font_size= 20))
        return grid
        # return Builder.load_file("calc.kv")
    
calc = Calc()
calc.run()