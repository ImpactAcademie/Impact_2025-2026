from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView

class SignupApp(App):

    def build(self):
        # Layout principal
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Titre
        layout.add_widget(Label(text="Inscription", font_size=32, size_hint=(1, None), height=40))

        # Champs pour l'email
        self.email_input = TextInput(hint_text="Email", size_hint_y=None, height=40)
        layout.add_widget(self.email_input)

        # Champs pour le mot de passe
        self.password_input = TextInput(hint_text="Mot de passe", password=True, size_hint_y=None, height=40)
        layout.add_widget(self.password_input)

        # Champs pour confirmer le mot de passe
        self.confirm_password_input = TextInput(hint_text="Confirmer le mot de passe", password=True, size_hint_y=None, height=40)
        layout.add_widget(self.confirm_password_input)

        # Bouton d'inscription
        signup_button = Button(text="S'inscrire", size_hint_y=None, height=50)
        signup_button.bind(on_press=self.on_signup)
        layout.add_widget(signup_button)

        return layout

    def on_signup(self, instance):
        # Récupération des valeurs des champs
        email = self.email_input.text
        password = self.password_input.text
        confirm_password = self.confirm_password_input.text

        # Validation simple
        if not email or not password or not confirm_password:
            self.show_popup("Erreur", "Tous les champs doivent être remplis.")
        elif password != confirm_password:
            self.show_popup("Erreur", "Les mots de passe ne correspondent pas.")
        elif while email not end by "@gmail.com" print false:
        else:
            # Ici on pourrait ajouter l'enregistrement des informations ou une vérification de l'email
            self.show_popup("Succès", "Inscription réussie !")

    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()

if __name__ == '__main__':
    SignupApp().run()
