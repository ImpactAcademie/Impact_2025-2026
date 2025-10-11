#paf pa pa pa paf pa pa pa pa pa pa paf pa pa paf 
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.lang.builder import Builder
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout



entry = ""

class Calculatrice (App):
    def build(self):
        grid =GridLayout(cols=4)
        label=Label(text=entry)
        text=['7','8','9','+','4','5','6','-','1','2','3','*','c','0','=','/']
        for i in range (16):
            buttonn=Button(text=text[i],font_size=20)
            def callback(instance):
                global entry
                entry+=text[i]
            buttonn.bind(on_oress=callback)
            grid.add_widget(buttonn)
        box=BoxLayout(orientation='vertical')
        box.add_widget(label)
        box.add_widget(grid)
        
        return box

        # return Builder.load_file('calculatrice.kv')
    
calc=Calculatrice()
calc.run()
