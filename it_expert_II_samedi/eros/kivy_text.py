from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
class BasicApp(App):
    def build(self):
        return Label(text='Bonjour est un mot qui veut dire ferme ta me la',pos_hint={'center_x':0.10,'center_y':0.8})
    
class ImageApp(App):
    def build(self):
        return Image(source='pokemonc.jpg')
    
app=ImageApp()
app.run()
