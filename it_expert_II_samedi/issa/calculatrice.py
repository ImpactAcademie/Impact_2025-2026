from kivy.app import App
from kivy.uix.button import Button 
from kivy.uix.gridlayout import GridLayout
from kivy.lang.builder import Builder

entry = " "


class Calculator(App):
    def build(self):
        grid = GridLayout(cols=4, padding=50, spacing=10)
        texts = ["7", "8", "9", "+", "4", "5", "6", "-", "1", "2", "3", "*" , "C", "0","=", "/"]
        for i  in range(16):
            def callback():
                entry+= texts[i]
            button = Button(text=texts[i], font_size=30)
            button.bind(on_press=callback)
            grid.add_widget(button)
        box = BoxLayout(orientation='vertical')
        box.add_widget(label)    
        box.add_widget(label)
        grid.add_widget(Button(text=texts[i], font_size=20))
        return grid 
        # return Builder.load_file("calculatrice.kv")
    
calc = Calculator()
calc.run()