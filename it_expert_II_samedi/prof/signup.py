from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import AsyncImage
from calculatrice import Calculator

class Signup(App):
    def build(self):
        logo = AsyncImage(source="https://cdn-icons-png.flaticon.com/512/5952/5952376.png")

        username_label = Label(text="Username", size_hint=(1, 0.5))
        username_input = TextInput(text="")
        
        password_label = Label(text="Password", size_hint=(1, 0.5))
        password_input = TextInput(text="")

        button_signup = Button(text="S'inscrire")
        button_signup.bind(on_press=click_signup)

        box = BoxLayout(orientation="vertical", spacing=10, padding=[400, 200, 400, 200])
        box.add_widget(logo)
        box.add_widget(username_label)
        box.add_widget(username_input)
        box.add_widget(password_label)
        box.add_widget(password_input)
        box.add_widget(button_signup)
        return box

class AppWindow(App):
    def build(self):
        return Label(text="Hello")

def click_signup(button):
    app.stop()
    page = Calculator()
    page.run()

app = Signup()
app.run()
