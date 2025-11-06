from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import AsyncImage
from calculatrice import Calculator

class signup(App):
    def build(self):
        logo = AsyncImage(source="https://tse2.mm.bing.net/th/id/OIP.XrGVljajcLZhvJGUD-Sc7gHaE7?cb=12&rs=1&pid=ImgDetMain&o=7&rm=3")
        pwInput = TextInput(text="")
        UserInput = TextInput(text="")

        UserLabel = Label(text="Email : ")
        pwLabel = Label(text="Mot de passe : ")

        buttonSignUp = Button(text="S'inscrire")
        buttonSignUp.bind(on_press = clickSignUp)

        box = BoxLayout(orientation="vertical", padding = [200,100,200,100], spacing = 30)
        box.add_widget(logo)
        
        box.add_widget(UserLabel)
        box.add_widget(UserInput)
        box.add_widget(pwLabel)
        box.add_widget(pwInput)
        box.add_widget(buttonSignUp)
        return box

class AppWindow:
    def build(self):
        return Label(text="Hello")


def clickSignUp(button):
    signUp.stop()
    page = Calculator()
    page.run()
    
    

signUp = signup()
signUp.run()