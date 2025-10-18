#paf pa pa pa paf pa pa pa pa pa pa paf pa pa paf 
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.lang.builder import Builder
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput




class Calculatrice (App):
    def build(self):
        label=TextInput(text='')
        grid =GridLayout(cols=4,padding=10,spacing=10)
        
        text=['7','8','9','+','4','5','6','-','1','2','3','*','c','0','=','/']
        for i in range (16):
            buttonn=Button(text=text[i],font_size=20)
            def callback(instance):
                if instance.text=='c':
                    label.text=''
                elif instance.text == '=' and label.text[-1] in ['*','-','+','/']:
                    return
                
                elif instance.text == '=' and not label.text[-1] in ['*','-','+','/']:
                    label.text=str(eval(label.text))
                
                elif instance.text in ['*','-','+','/'] and label.text[-1] in ['*','-','+','/']:
                    return
                else:
                    label.text+=instance.text
            buttonn.bind(on_press=callback)
            grid.add_widget(buttonn)
        box=BoxLayout(orientation='vertical')
        box.add_widget(label)
        box.add_widget(grid)
        
        return box

        # return Builder.load_file('calculatrice.kv')

if __name__=="__main__":

    calc=Calculatrice()
    calc.run()






