from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image, AsyncImage
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

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


app = ImageApp()
app.run()