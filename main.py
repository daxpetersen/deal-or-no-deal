from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from random import shuffle
import random
from kivy.lang import Builder
list = [.01,.1,1,10,100,1000,10000,100000,1000000]
class DealOrNoDealApp(App):
    def build(self):
        self.x =0
        return  Builder.load_file('main.kv')
    def make_deal(self):
        self.number = random.randint(1,len(list)-1)
        self.number = list[self.number]
        print(self.number)
        spot = list.index(self.number)
        list.pop(spot)
    def word(self):
        return "Deal"
        
if __name__ == "__main__":
    DealOrNoDealApp().run()