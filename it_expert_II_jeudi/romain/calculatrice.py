from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image, AsyncImage
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout

class BasicApp(App):
    def build(self):
        return Label(text="Au revoir tout le monde", 
                     size_hint=(0.5, 0.5),
                     pos_hint={'center_x': 0.01, 'center_y': 0.9})

class ImageApp(App):
    def build(self):
        return AsyncImage(source="https://sm.ign.com/ign_fr/cover/t/the-legend/the-legend-of-aang-the-last-airbender_d9c8.jpg",
                     size_hint=(1, 1))
    
class HBoxLayout(App):
    def build(self):
        layout = BoxLayout(padding=10)
        for i in range(5):
            layout.add_widget(Button(text="Bouton", background_color=[1, 0, 0, 1]))
        return layout
    
class Calculator(App):
    def build(self):
        textinput = TextInput()

        grid = GridLayout(cols=4)
        values = ["7", "8", "9", "+", "4", "5", "6", "*", "1", "2", "3", "-", "C", "0", "=", "/"]
        def add_value(instance):
            if instance.text == "C":
                textinput.text = ""
            elif instance.text == "=":
                textinput.text = str(eval(textinput.text))
            else:
                textinput.text += instance.text
        for v in values:
            button = Button(text=v, background_color=(1, 0.07, 0.57, 1))
            button.bind(on_press=add_value)
            grid.add_widget(button)
      
        layout = BoxLayout(orientation="vertical")
        layout.add_widget(textinput)
        layout.add_widget(grid)

        return layout 


app = Calculator()
app.run()

