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

food_dict = {
             #Фруктовые
             'Апельсин':(0.43, 0.009, 0.002, 0.081), 'Банан':(0.96, 0.015, 0.005, 0.21), 'Чернослив':(110/45, 1/45, 0, 29/45),
             'Курага':(100/40, 1/40, 0, 24/40), 'Изюм':(140/40, 1/40, 0, 33/40),
             #Молочные
             'Пармезан':(110/28, 8/28, 8/28, 0), 'Швейцарский':(80, 6/22, 6/22, 0), 'Сырок':(140, 8, 7, 13), 'Масло':(100/14,0,11/14,0),
             'Уй':(160,1/141,8/141,19/141),   
             #Сладкое
             'Мёд':(60/21,0,0,17/21), 'Эклер':(43.33,0.67,2.67,6), 'Профитроль':(45,0.67,3.5,2.67),
             'Стандарт':(1,0,0,0)} #'Название':(калории, белки, жиры, углеводы)

mainmenuFsize = 80

dropdown = DropDown()
           
class MainApp(App):
    food_sorter = {}
    def sorter(self):
        # if self.textinput1.text == '':
        #     self.food_sorter = food_dict
        # else:
            for key,value in food_dict.items():
                if key[0] == self.textinput1.text.upper():
                    self.food_sorter[key]=value
                else:
                    pass
                
    def dropdownmenu(self, dictionary, *args):
        dropdown.clear_widgets()
                
        for key in dictionary:
            btn = Button(text=key, font_size=mainmenuFsize, size_hint_y=None, height=120) #
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)        
        
    def build(self):
            #Elements        
        img = Image(source='Fenix.jpg')
        
        self.label = Label(text='0', font_size=320, bold=True, pos_hint={'center_x': .5, 'center_y': .5}) #size_hint=(None, None), 
        
        self.textinput1 = TextInput(text='', multiline=False, font_size=170, size_hint=(0.125, 0.5))
        
        self.dropdownmenu(food_dict)
        
        self.mainbutton = Button(text='Стандарт', font_size=mainmenuFsize, size_hint=(0.5, 0.5)) #
        
        dropdown.bind(on_select=lambda instance, x: setattr(self.mainbutton, 'text', x))
        
        self.textinput = TextInput(text='', multiline=False, font_size=170, size_hint=(0.25, 0.5)) #
        
        btnAdd = Button(text='+', font_size=mainmenuFsize, size_hint=(0.125, 0.5)) #, size_hint=(None, None)
                
        self.label1 = Label(text='Filler', color=(0,0,0,255), pos_hint={'center_x': .5, 'center_y': .5}) # 
        self.label2 = Label(text='Filler', color=(0,0,0,255), pos_hint={'center_x': .5, 'center_y': .5})
        
            #Main Layout
        layoutMain = BoxLayout(padding=10, orientation='vertical')
        
            #Primary Layout
        layoutPri = BoxLayout(padding=10, orientation='horizontal')
        layoutPri.add_widget(self.label)
            #Auxilary Layout
        layoutAux = BoxLayout(padding=10, orientation='horizontal')
        layoutAux.add_widget(self.textinput1)
        layoutAux.add_widget(self.mainbutton)
        layoutAux.add_widget(self.textinput)
        layoutAux.add_widget(btnAdd)
            #Auxilary 1 Layout
        layoutAux1 = BoxLayout(padding=10, orientation='horizontal')
        layoutAux1.add_widget(self.label1)
            #Auxilary 2 Layout
        layoutAux2 = BoxLayout(padding=10, orientation='horizontal')
        layoutAux2.add_widget(self.label2)
        
        layoutMain.add_widget(img)
        layoutMain.add_widget(layoutPri)
        layoutMain.add_widget(layoutAux)
        layoutMain.add_widget(layoutAux1)
        layoutMain.add_widget(layoutAux2)
        
        btnAdd.bind(on_press=self.on_press_add_button)
        self.mainbutton.bind(on_release=dropdown.open)
        
        def reset(*args):
            self.textinput1.text = ''
            self.dropdownmenu(food_dict)
        
        def menucreator(*args):
            self.food_sorter = {}
            self.sorter()
            self.dropdownmenu(self.food_sorter)
                   
        dropdown.bind(on_select=lambda instance, x: setattr(self.mainbutton, 'text', x))
        self.textinput1.bind(text=menucreator, on_text_validate=reset)
        
        return layoutMain
                    
    def on_press_add_button(self, instance):
        if self.textinput.text.isdigit() == True:
            self.label.text = str(round(float(self.label.text) + float(self.textinput.text)*food_dict[self.mainbutton.text][0]))
            self.textinput.text = ''
            self.textinput1.text = ''
            self.dropdownmenu(food_dict)
        else:
            pass

        
if __name__ == '__main__':
    app = MainApp()
    app.run()