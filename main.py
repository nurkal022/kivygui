import kivy
from kivy import Config
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty

Config.set("graphics","width",900)
Config.set("graphics","height",400)

class Container(GridLayout):
    text_input=ObjectProperty()
    lable_widget=ObjectProperty()

    def change_text(self):
        self.lable_widget.text=(self.text_input.text).upper()

class MyApp(App):
    def build(self):
        return Container()


if __name__ == '__main__':
     
    MyApp().run()