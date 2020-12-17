# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 00:48:54 2020

@author: vntom
"""

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

from kivy.core.text import LabelBase

LabelBase.register(name='Cyrillic_2', fn_regular='Cyrillic_2.ttf')

food_dict = {
             #Фруктовые
             'Апельсин':(0.43, 0.009, 0.002, 0.081), 'Банан':(0.96, 0.015, 0.005, 0.21), 'Чернослив':(110/45, 1/45, 0, 29/45),
             'Курага':(100/40, 1/40, 0, 24/40), 'Изюм':(140/40, 1/40, 0, 33/40),
             #Молочные
             'Пармезан':(110/28, 8/28, 8/28, 0), 'Швейцарский':(80, 6, 6, 0), 'Сырок':(140, 8, 7, 13), 'Масло':(100/14,0,11/14,0),
             'Уй':(160,1,8,19),   
             #Сладкое
             'Мед':(60/21,0,0,17/21), 'Эклер':(43.33,0.67,2.67,6), 'Профитроль':(45,0.67,3.5,2.67),
             'Стандарт':(1,0,0,0)} #'Название':(калории, белки, жиры, углеводы)}

food_sorter = {}

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
            btn = Button(text=key, font_name='Cyrillic_2', font_size=mainmenufontsize, size_hint_y=None, height=120) #
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)            

    def build(self):
            #Elements        
        reset_button = Button(background_normal='Fenix.jpg', background_down='Fenix.jpg', size_hint=(0.65,1), pos_hint={'center_x': .5, 'center_y': .5})
                
        #Added numerical labels
        self.calories_label = Label(text='0', font_name='Cyrillic_2', font_size=300, bold=True, pos_hint={'center_x': .5, 'center_y': .5}) #size_hint=(None, None), 
        self.calories_text_label = Label(text='ккал', font_name='Cyrillic_2', font_size=200, pos_hint={'center_x': .5, 'center_y': .5}) #size_hint=(None, None),
        self.protein_label = Label(text='0 белков', color=(1,1,1,1), font_name='Cyrillic_2', font_size=80, pos_hint={'center_x': .5, 'center_y': .5})
        self.fat_label = Label(text='0 жиров', color=(1,1,0,1), font_name='Cyrillic_2', font_size=80, pos_hint={'center_x': .5, 'center_y': .5})
        self.carb_label = Label(text='0 углеводов', color=(1,0,0,1), font_name='Cyrillic_2', font_size=80, pos_hint={'center_x': .5, 'center_y': .5})
        
        self.search_input = TextInput(text='а', multiline=False, font_size=170, size_hint=(0.125, 0.5))
        
        self.selection_button = Button(text='Стандарт', font_name='Cyrillic_2', font_size=mainmenufontsize, size_hint=(0.5, 0.5)) #
        
        self.portion_input = TextInput(multiline=False, font_name='Cyrillic_2', font_size=170, size_hint=(0.25, 0.5)) 
        
        add_button = Button(text='+', font_name='Cyrillic_2', font_size=mainmenufontsize, size_hint=(0.125, 0.5)) #, size_hint=(None, None)
                
        self.calories_base_label = Label(text='', color=(1,1,1,0.6), font_name='Cyrillic_2', font_size=200, pos_hint={'center_x': .5, 'center_y': .5})
        self.calories_text1_label = Label(text='', color=(1,1,1,0.6), font_name='Cyrillic_2', font_size=100, pos_hint={'center_x': .5, 'center_y': .5})
        self.protein_base_label = Label(text='', color=(1,1,1,0.6), font_name='Cyrillic_2', font_size=70) #, pos_hint={'center_x': .5, 'center_y': .5}
        self.fat_base_label = Label(text='', color=(1,1,0,0.6), font_name='Cyrillic_2', font_size=70) #, pos_hint={'center_x': .5, 'center_y': .5}
        self.carb_base_label = Label(text='', color=(1,0,0,0.6), font_name='Cyrillic_2', font_size=70) #, pos_hint={'center_x': .5, 'center_y': .5}

        self.spacer = Label(text='Filler', color=[0,0,0,0], pos_hint={'center_x': .5, 'center_y': .5}) # [255,255,255,255]
        
            #Calorie Box
        caloriebox = BoxLayout(padding=20, orientation='vertical')
        #Calorie Elements
        caloriebox.add_widget(self.calories_label)
        caloriebox.add_widget(self.calories_text_label)
                
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
        
        #Calorie_base Box
        caloriebasebox = BoxLayout(padding=20, orientation='vertical')
        #Calorie Elements
        caloriebasebox.add_widget(self.calories_base_label)
        caloriebasebox.add_widget(self.calories_text1_label)
        
        #P/F/C_base Box
        pfcbasebox = BoxLayout(padding=0, orientation='vertical')
        #P/F/C_base Elements
        pfcbasebox.add_widget(self.protein_base_label)
        pfcbasebox.add_widget(self.fat_base_label)
        pfcbasebox.add_widget(self.carb_base_label)
        
            #Row 4
        row4 = BoxLayout(padding=0, orientation='horizontal')
        row4.add_widget(caloriebasebox)
        row4.add_widget(pfcbasebox)
        
            #Row 5
        row5 = BoxLayout(padding=0, orientation='horizontal')
        row5.add_widget(self.spacer)
        
            #Main Layout
        mainlayout = BoxLayout(padding=0, orientation='vertical')
        #Main Elements
        mainlayout.add_widget(reset_button)
        mainlayout.add_widget(row2)
        mainlayout.add_widget(row3)
        mainlayout.add_widget(row4)
        mainlayout.add_widget(row5)

        def total_reset(*args):
            self.calories_label.text = '0'
            self.protein_label.text = '0 белков'
            self.fat_label.text = '0 жиров'
            self.carb_label.text = '0 углеводов'
            self.search_input.text = ''
            self.dropdownmenu(food_dict)
            
        reset_button.bind(on_press=total_reset)
        add_button.bind(on_press=self.on_press_add_button)
        self.selection_button.bind(on_release=dropdown.open)

        def reset(*args):
            self.search_input.text = ''
            self.dropdownmenu(food_dict)
        
        def menucreator(*args):
            self.food_sorter = {}
            self.sorter()
            self.dropdownmenu(self.food_sorter)
        
        #dropdown.bind(on_select=lambda instance, x: setattr(self.selection_button, 'text', x))
        def dropdownbind(instance, x):
            setattr(self.selection_button, 'text', x) #setattr(object, name, value) - sets value of an attribute of an object
            
        def base(instance, x):
            if x == '':
                self.calories_base_label.text = ''
                self.calories_text1_label.text = ''
                self.protein_base_label.text = ''
                self.fat_base_label.text = ''
                self.carb_base_label.text = ''
            else:    
                self.calories_base_label.text = str(round((float(x)*food_dict[self.selection_button.text][0])))
                self.calories_text1_label.text = 'ккал'
                self.protein_base_label.text = str(round((float(x)*food_dict[self.selection_button.text][1])))+' белков'
                self.fat_base_label.text = str(round((float(x)*food_dict[self.selection_button.text][2]))) +' жиров'
                self.carb_base_label.text = str(round((float(x)*food_dict[self.selection_button.text][3]))) +' углеводов'
    
        dropdown.bind(on_select=dropdownbind)
        self.search_input.bind(text=menucreator, on_text_validate=reset)
        self.portion_input.bind(text=base)
        self.search_input.text = ''
        self.dropdownmenu(food_dict)
        
        return mainlayout
                    
    def on_press_add_button(self, instance):
        
        if self.portion_input.text.isdigit() == True:
            self.calories_label.text = str(round(float(self.calories_label.text.split()[0]) + float(self.portion_input.text)*food_dict[self.selection_button.text][0]))
            self.protein_label.text = str(round(float(self.protein_label.text.split()[0]) + float(self.portion_input.text)*food_dict[self.selection_button.text][1]))+' белков'
            self.fat_label.text = str(round(float(self.fat_label.text.split()[0]) + float(self.portion_input.text)*food_dict[self.selection_button.text][2]))+' жиров'
            self.carb_label.text = str(round(float(self.carb_label.text.split()[0]) + float(self.portion_input.text)*food_dict[self.selection_button.text][3]))+' углеводов'
            self.portion_input.text = ''
            self.search_input.text = ''
            self.dropdownmenu(food_dict)
        else:
            pass
    
if __name__ == '__main__':
    MainApp().run()