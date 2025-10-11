from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
class BasicApp(App):
    def build(self):
        return Label(text="Bonjour tout le monde",pos_hint ={"center_x":0.1, "center_y":0.8})
    
class ImageApp(App):
    def build(self):
        return Image(source="x.webp")
    

    
app = ImageApp()
app.run()