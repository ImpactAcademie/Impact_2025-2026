from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import AsyncImage

class Signup(App):
    def build(self):
        logo = AsyncImage(src="https://i.redd.it/vewwqeyihbaf1.jpeg")
        label = Label(text = "")
        sign = Button(text = "Sign Up")

        username_label = Label(text="Username")
        username_input = TextInput(text="")
        password_label = Label(text="Password")
        password_input = TextInput(text="")
        box.add_widget(logo)

        box = BoxLayout(orientation="vertical", padding=[350, 200, 350, 200], spacing=30)

        box.add_widget(username_label)
        box.add_widget(username_input)
        box.add_widget(password_label)
        box.add_widget(password_input)
        # box.add_widget(label)
        box.add_widget(sign)
        # box.add_widget(grid)
        return box
class AppWindow(App):

app = Signup()
app.run()