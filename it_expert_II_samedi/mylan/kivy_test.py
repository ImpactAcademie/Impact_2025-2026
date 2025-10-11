from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image


class BasicApp(App):
    def build(self):
        return Label(text="bonjour", pos_hint={"center_x":0.5, "center_y":0.5})
    

class ImageApp(App):
    def build(self):
        return Image(source="sparta.jpg")
    
    
    
app = ImageApp()
app.run()    