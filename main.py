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
             'Стандарт':(1,0,0,0)} #'Название':(калории, белки, жиры, углеводы)}

food_sorter = {}

caloriecount = 0
proteincount = 0
fatcount = 0
carbcount = 0 

mainmenufontsize = 80

dropdown = DropDown()
           
class MainApp(App):

    def sorter(self):
        for key,value in food_dict.items():
            if key[0] == self.search_input.text.upper():
                self.food_sorter[key]=value
            else:
                pass
                
    def dropdownmenu(self, dictionary, *args):
        
        dropdown.clear_widgets()
        
        for key in dictionary:
            btn = Button(text=key, font_size=mainmenufontsize, size_hint_y=None, height=120) #
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)            

    def build(self):
            #Elements        
        logo = Image(source='Fenix.jpg')
        #Text labels
        
        #Added numerical labels
        self.calories_label = Label(text=str(caloriecount)+' ккал', font_size=320, bold=True, pos_hint={'center_x': .5, 'center_y': .5}) #size_hint=(None, None), 
        self.protein_label = Label(text=str(proteincount)+' белков', color=(1,1,1,1), font_size=100, bold=True, pos_hint={'center_x': .5, 'center_y': .5})
        self.fat_label = Label(text=str(fatcount)+' жиров', color=(1,1,0,1), font_size=100, bold=True, pos_hint={'center_x': .5, 'center_y': .5})
        self.carb_label = Label(text=str(carbcount)+' углеводов', color=(1,0,0,1), font_size=100, bold=True, pos_hint={'center_x': .5, 'center_y': .5})
        
        self.search_input = TextInput(text='а', multiline=False, font_size=170, size_hint=(0.125, 0.5))
        
        self.selection_button = Button(text='Стандарт', font_size=mainmenufontsize, size_hint=(0.5, 0.5)) #
        
        dropdown.bind(on_select=lambda instance, x: setattr(self.selection_button, 'text', x))
        
        self.portion_input = TextInput(multiline=False, font_size=170, size_hint=(0.25, 0.5)) 
        
        add_button = Button(text='+', font_size=mainmenufontsize, size_hint=(0.125, 0.5)) #, size_hint=(None, None)
                
        self.spacer1 = Label(text='Filler', color=[0,0,0,0], pos_hint={'center_x': .5, 'center_y': .5}) # [255,255,255,255]
        self.spacer2 = Label(text='Filler', color=[0,0,0,0], pos_hint={'center_x': .5, 'center_y': .5}) #, color=(0,0,0,255)


            #Calorie Box
        caloriebox = BoxLayout(padding=0, orientation='horizontal')
        #Calorie Elements
        caloriebox.add_widget(self.calories_label)
                
            #P/F/C Elements
       
         #P/F/C Box
        pfcbox = BoxLayout(padding=0, orientation='vertical')
        pfcbox.add_widget(self.protein_label)
        pfcbox.add_widget(self.fat_label)
        pfcbox.add_widget(self.carb_label)
        
            #Row 2
        row2 = BoxLayout(padding=0, orientation='horizontal')
        #Row 2 Elements
        row2.add_widget(caloriebox)
        row2.add_widget(pfcbox)

            #Row 3
        row3 = BoxLayout(padding=0, orientation='horizontal')
        #Row 3 Elements
        row3.add_widget(self.search_input)
        row3.add_widget(self.selection_button)
        row3.add_widget(self.portion_input)
        row3.add_widget(add_button)
        
            #Row 4 Layout
        row4 = BoxLayout(padding=0, orientation='horizontal')
        row4.add_widget(self.spacer1)
        
            #Row 5 Layout
        row5 = BoxLayout(padding=0, orientation='horizontal')
        row5.add_widget(self.spacer2)
        
           #Main Layout
        mainlayout = BoxLayout(padding=0, orientation='vertical')
        #Main Elements
        mainlayout.add_widget(logo)
        mainlayout.add_widget(row2)
        mainlayout.add_widget(row3)
        mainlayout.add_widget(row4)
        mainlayout.add_widget(row5)
        
        add_button.bind(on_press=self.on_press_add_button)
        self.selection_button.bind(on_release=dropdown.open)
        
        def reset(*args):
            self.search_input.text = ''
            self.dropdownmenu(food_dict)
        
        def menucreator(*args):
            self.food_sorter = {}
            self.sorter()
            self.dropdownmenu(self.food_sorter)
            
                   
        dropdown.bind(on_select=lambda instance, x: setattr(self.selection_button, 'text', x))
        self.search_input.bind(text=menucreator, on_text_validate=reset)
        
        self.search_input.text = ''
        self.dropdownmenu(food_dict)
        
        return mainlayout
                    
    def on_press_add_button(self, instance):
        if self.portion_input.text.isdigit() == True:
            self.calories_label.text = str(round(float(caloriecount) + float(self.portion_input.text)*food_dict[self.selection_button.text][0]))+' ккал'
            self.protein_label.text = str(round(float(proteincount) + float(self.portion_input.text)*food_dict[self.selection_button.text][1]))+' белков'
            self.fat_label.text = str(round(float(fatcount) + float(self.portion_input.text)*food_dict[self.selection_button.text][2]))+' жиров'
            self.carb_label.text = str(round(float(carbcount) + float(self.portion_input.text)*food_dict[self.selection_button.text][3]))+' углеводов'
            self.portion_input.text = ''
            self.search_input.text = ''
            self.dropdownmenu(food_dict)
        else:
            pass
    
if __name__ == '__main__':
    MainApp().run()