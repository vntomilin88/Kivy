# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 00:48:54 2020

@author: vntom
"""
import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput


food_dict = {'Сырок': 140, 'Апельсин': 0.43, 'Яйцо': 80}
coefficient = ''

           
class MainApp(App):
    def build(self):
            #Elements        
        img = Image(source='Fenix.jpg')
        
        self.label = Label(text='0', font_size=180, bold=True, pos_hint={'center_x': .5, 'center_y': .5}) #size_hint=(None, None), 
        
        dropdown = DropDown()
        for key in food_dict:
            
            btn = Button(text=key, size_hint_y=None, height=80) #
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)
        
        self.mainbutton = Button(text='Sustenance') #, size_hint=(0.3, None)
        
        dropdown.bind(on_select=lambda instance, x: setattr(self.mainbutton, 'text', x))
        
        self.textinput = TextInput(text='', multiline=False, font_size=120) #, size_hint=(0.3, 0.2)
        
        btnAdd = Button(text="Add Up") #, size_hint=(None, None)
                
        #self.label1 = Label(text='1', pos_hint={'center_x': .5, 'center_y': .5})
        #self.label2 = Label(text='', pos_hint={'center_x': .5, 'center_y': .5})
        
            #Main Layout
        layoutMain = BoxLayout(padding=10, orientation='vertical')
        
            #Primary Layout
        layoutPri = BoxLayout(padding=10, orientation='horizontal')
        layoutPri.add_widget(self.label)
            #Auxilary Layout
        layoutAux = BoxLayout(padding=10, orientation='horizontal')
        layoutAux.add_widget(self.mainbutton)
        layoutAux.add_widget(self.textinput)
        layoutAux.add_widget(btnAdd)
            #Auxilary 1 Layout
        #layoutAux1 = BoxLayout(padding=10, orientation='horizontal')
        #layoutAux1.add_widget(self.label1)
            #Auxilary 2 Layout
        #layoutAux2 = BoxLayout(padding=10, orientation='horizontal')
        #layoutAux2.add_widget(self.label2)
        
        layoutMain.add_widget(img)
        layoutMain.add_widget(layoutPri)
        layoutMain.add_widget(layoutAux)
        #layoutMain.add_widget(layoutAux1)
        #layoutMain.add_widget(layoutAux2)
        
        btnAdd.bind(on_press=self.on_press_button)
        self.mainbutton.bind(on_release=dropdown.open)
        
                   
        dropdown.bind(on_select=lambda instance, x: setattr(self.mainbutton, 'text', x))
               
        return layoutMain
        
            
    def on_press_button(self, instance):
        self.label.text = str(float(self.label.text) + float(self.textinput.text)*food_dict[self.mainbutton.text])
        self.textinput.text = ''

   
            
if __name__ == '__main__':
    app = MainApp()
    app.run()