import kivy
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.lang.builder import Builder
Builder.load_string(
    '''
<MygridLayout>
    BoxLayout
        orientation:"vertical"
        size:root.width,root.height
        
        Label:
            text:"base"
            id:shiva
            font_size:34
        TextInput:
            multiline:True
            id:kirshna
        Button:
            text:"submit"
            on_press:root.submit()
            
    
    
    
    
    '''
)
class Mygridlayout(Widget):

    def submit(self):
        pre = self.ids.kirshna.text
        self.ids.shiva.text = pre






class maapp(App):
    def build(self):
        return  Mygridlayout()
if __name__=='__main__':
    maapp().run()