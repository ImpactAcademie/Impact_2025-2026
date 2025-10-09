from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
class codeurApp(App):
    def build(self):
        return Label(text="designed by ayoub",
                     size_hint=(0.5, 0.5),
                     pos_hint={'center_x': 0.01, 'center_y': 0.9})
class ImageApp(App):
    def build(self):
        return Image(source="image.png",
                     size_hint=(0.5, 0.3))
class HBoxLayout(App):
    def build(self):
        layout = BoxLayout(padding=10)
        for i in range(5):
            layout.add_widget(Button(text="Button", background_color=[1, 0, 0, 1]))
        return layout

app = HBoxLayout()
app.run()