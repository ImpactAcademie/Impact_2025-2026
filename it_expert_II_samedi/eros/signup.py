from dis import Instruction
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.lang.builder import Builder
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import AsyncImage
from calculatrice import Calculatrice


#___________def class___________

class Inscriptionnn(App):
    def build(self):
    

    

#padding= vertical

    

# _______________variable___________ 

    
        logo=AsyncImage(source='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMOF5JapMpayeeOwR6d44dOyyHfwuCf4BunA&s')
        label_text=Label(text="nom d'utilisateur",size_hint=(1,0.5))
        label_input=TextInput(text='')
        pwd_text=Label(text="mot de passe")
        pwd_input=TextInput(text='')
        button_enscrire=Button(text="s'inscrire")
        button_enscrire.bind(on_press=click_signup)
    

#_____________affichage_texte___________

        box=BoxLayout(orientation='vertical', padding=(200,200,200,200),spacing=10)
        box.add_widget(label_text)
        box.add_widget(label_input)
        box.add_widget(pwd_text)
        box.add_widget(pwd_input)
        box.add_widget(button_enscrire)

        return box

    

class AppWindow(App):

    def build(self):
        return Label(text='hello')
    
def click_signup(button):
    app.stop()
    page = AppWindow()
    page.run()

if __name__=="__main__":

    app=Inscriptionnn()
    app.run()
    

    