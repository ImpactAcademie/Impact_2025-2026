from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class Signup(App):
    def build(self):
        username_label = Label(text="username")
        username_input = TextInput(text="")

        password_label = Label(text="username")
        password_input = TextInput(text="")

        button_signup = Button(text="S'inscrire")

        box = BoxLayout(orientation="vertical", spacing=10, padding=[400, 200, 400, 200])
        box.add_widget(username_label)
        box.add_widget(username_input)
        box.add_widget(password_label)
        box.add_widget(password_input)
        box.add_widget(button_signup)
        return box
    
app = Signup()
app.run()