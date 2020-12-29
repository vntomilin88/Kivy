# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 00:48:54 2020

@author: vntom
"""

#from kivy.config import Config
# Config.set('kivy', 'default_font', ["Arial", "C:/Windows/Fonts/arial.ttf", "C:/Windows/Fonts/ariali.ttf", "C:/Windows/Fonts/arialbd.ttf", "C:/Windows/Fonts/arialbi.ttf"])
#Config.set('kivy', 'default_font', ['Izhitsa', 'Izhitsa.ttf'])
#Config.write() 

from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.uix.carousel import Carousel
from kivy.uix.dropdown import DropDown
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.vkeyboard import VKeyboard
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout

 
LabelBase.register(name='Teremok', fn_regular='Teremok.ttf') #, fn_bold=''
#VKeyboard.layout = 'numeric.json'

food_dict = {
             #Фруктовые
             'Апельсин':(0.43, 0.009, 0.002, 0.081), 'Банан':(0.96, 0.015, 0.005, 0.21), 'Чернослив':(110/45, 1/45, 0, 29/45),
             'Курага':(100/40, 1/40, 0, 24/40), 'Изюм':(140/40, 1/40, 0, 33/40),
             #Молочные
             'Пармезан':(110/28, 8/28, 8/28, 0), 'Швейцарский':(80, 6, 6, 0), 'Сырок':(140, 8, 7, 13), 'Масло':(100/14,0,11/14,0),
             'Уй':(160,1,8,19),   
             #Сладкое
             'Мёд':(60/21,0,0,17/21), 'Эклер':(43.33,0.67,2.67,6), 'Профитроль':(45,0.67,3.5,2.67),
             'Стандарт':(1,0,0,0)} #'Название':(калории, белки, жиры, углеводы)}

food_sorter = {}

mainmenufontsize = 120
teremokfont = 'Teremok'


#DIETCOUNTERSCREEN
DietCounterScreen = Screen(name='DietCounter')

dropdown = DropDown()

def sorter():
    for key,value in food_dict.items():
        if key[0] == search_input.text.upper():
            food_sorter[key]=value
        else:
            pass
                
def dropdownmenu(dictionary, *args):
     
     dropdown.clear_widgets()
     
     for key in dictionary:
         btn = Button(text=key, background_color=(0,0,0,1), font_name=teremokfont, font_size=mainmenufontsize, size_hint_y=None) #, height=120
         btn.bind(on_release=lambda btn: dropdown.select(btn.text))
         dropdown.add_widget(btn)            


    #Elements        
reset_button = Button(background_normal='Fenix.jpg', background_down='Fenix.jpg', size_hint=(0.65,1), pos_hint={'center_x': .5, 'center_y': .5})
        
#Added numerical labels
calories_label = Label(text='0', font_name=teremokfont, font_size=300, pos_hint={'center_x': .5, 'center_y': .5}) #size_hint=(None, None), bold=False, 
calories_text_label = Label(text='ккал', font_name=teremokfont, font_size=200, pos_hint={'center_x': .5, 'center_y': .5}) #size_hint=(None, None),
protein_label = Label(text='0 белков', font_name=teremokfont, color=(1,1,1,1), font_size=80, pos_hint={'center_x': .5, 'center_y': .5})
fat_label = Label(text='0 жиров', font_name=teremokfont, color=(1,0.874,0,1),  font_size=80, pos_hint={'center_x': .5, 'center_y': .5})
carb_label = Label(text='0 углеводов', font_name=teremokfont, color=(0.65,0,0.12,1), font_size=80, pos_hint={'center_x': .5, 'center_y': .5})

search_input = TextInput(text='а', font_name=teremokfont, foreground_color=(1,1,1,1), background_color=(0,0,0,0), multiline=False, font_size=120, size_hint=(0.125, 0.5))

selection_button = Button(text='Стандарт', background_color=(0,0,0,0), font_name=teremokfont, font_size=mainmenufontsize, size_hint=(0.5, 0.5)) #

portion_input = TextInput(multiline=False, background_color=(0,0,0,0), font_name=teremokfont,  foreground_color=(1,1,1,1), font_size=120, size_hint=(0.25, 0.5)) 

add_button = Button(text='+', background_color=(0,0,0,0), font_name=teremokfont, font_size=mainmenufontsize, size_hint=(0.125, 0.5)) #, size_hint=(None, None)
        
calories_base_label = Label(text='',font_name=teremokfont, color=(1,1,1,0.6),  font_size=200, pos_hint={'center_x': .5, 'center_y': .5})
calories_text1_label = Label(text='', font_name=teremokfont, color=(1,1,1,0.6),  font_size=100, pos_hint={'center_x': .5, 'center_y': .5})
protein_base_label = Label(text='', font_name=teremokfont, color=(1,1,1,0.6),  font_size=70) #, pos_hint={'center_x': .5, 'center_y': .5}
fat_base_label = Label(text='', font_name=teremokfont, color=(1,0.874,0,0.6),  font_size=70) #, pos_hint={'center_x': .5, 'center_y': .5}
carb_base_label = Label(text='', font_name=teremokfont, color=(0.65,0,0.12,0.6),  font_size=70) #, pos_hint={'center_x': .5, 'center_y': .5}

spacer = Label(text='Filler', font_name=teremokfont, color=(0,0,0,0), pos_hint={'center_x': .5, 'center_y': .5}) # [255,255,255,255]

    #Calorie Box
caloriebox = BoxLayout(padding=20, orientation='vertical')
#Calorie Elements
caloriebox.add_widget(calories_label)
caloriebox.add_widget(calories_text_label)
        
    #P/F/C Elements
   
#P/F/C Box
pfcbox = BoxLayout(padding=0, orientation='vertical')
pfcbox.add_widget(protein_label)
pfcbox.add_widget(fat_label)
pfcbox.add_widget(carb_label)

    #Row 2
row2 = BoxLayout(padding=0, orientation='horizontal')
#Row 2 Elements
row2.add_widget(caloriebox)
row2.add_widget(pfcbox)

    #Row 3
row3 = BoxLayout(padding=0, orientation='horizontal')
#Row 3 Elements
row3.add_widget(search_input)
row3.add_widget(selection_button)
row3.add_widget(portion_input)
row3.add_widget(add_button)

#Calorie_base Box
caloriebasebox = BoxLayout(padding=20, orientation='vertical')
#Calorie Elements
caloriebasebox.add_widget(calories_base_label)
caloriebasebox.add_widget(calories_text1_label)

#P/F/C_base Box
pfcbasebox = BoxLayout(padding=0, orientation='vertical')
#P/F/C_base Elements
pfcbasebox.add_widget(protein_base_label)
pfcbasebox.add_widget(fat_base_label)
pfcbasebox.add_widget(carb_base_label)

    #Row 4
row4 = BoxLayout(padding=0, orientation='horizontal')
row4.add_widget(caloriebasebox)
row4.add_widget(pfcbasebox)

    #Row 5
row5 = BoxLayout(padding=0, orientation='horizontal')
row5.add_widget(spacer)

    #Main Layout
mainlayout = BoxLayout(padding=0, orientation='vertical')
#Main Elements
mainlayout.add_widget(reset_button)
mainlayout.add_widget(row2)
mainlayout.add_widget(row3)
mainlayout.add_widget(row4)
mainlayout.add_widget(row5)

def total_reset(*args):
    calories_label.text = '0'
    protein_label.text = '0 белков'
    fat_label.text = '0 жиров'
    carb_label.text = '0 углеводов'
    search_input.text = ''
    dropdownmenu(food_dict)
    
def reset(*args):
    search_input.text = ''
    dropdownmenu(food_dict)

def menucreator(*args):
    food_sorter = {}
    sorter()
    dropdownmenu(food_sorter)

#dropdown.bind(on_select=lambda instance, x: setattr(selection_button, 'text', x))
def dropdownbind(instance, x):
    setattr(selection_button, 'text', x) #setattr(object, name, value) - sets value of an attribute of an object
    
def base(instance, x):
    if x == '':
        calories_base_label.text = ''
        calories_text1_label.text = ''
        protein_base_label.text = ''
        fat_base_label.text = ''
        carb_base_label.text = ''
    else:    
        calories_base_label.text = str(round((float(x)*food_dict[selection_button.text][0])))
        calories_text1_label.text = 'ккал'
        protein_base_label.text = str(round((float(x)*food_dict[selection_button.text][1]))) +' белков'
        fat_base_label.text = str(round((float(x)*food_dict[selection_button.text][2]))) +' жиров'
        carb_base_label.text = str(round((float(x)*food_dict[selection_button.text][3]))) +' углеводов'

dropdown.bind(on_select=dropdownbind)
search_input.bind(text=menucreator, on_text_validate=reset)
portion_input.bind(text=base)
search_input.text = ''
dropdownmenu(food_dict)

                 
def on_press_add_button(instance):
     
     if portion_input.text.isdigit() == True:
         calories_label.text = str(round(float(calories_label.text.split()[0]) + float(portion_input.text)*food_dict[selection_button.text][0]))
         protein_label.text = str(round(float(protein_label.text.split()[0]) + float(portion_input.text)*food_dict[selection_button.text][1]))+' белков'
         fat_label.text = str(round(float(fat_label.text.split()[0]) + float(portion_input.text)*food_dict[selection_button.text][2]))+' жиров'
         carb_label.text = str(round(float(carb_label.text.split()[0]) + float(portion_input.text)*food_dict[selection_button.text][3]))+' углеводов'
         portion_input.text = ''
         search_input.text = ''
         dropdownmenu(food_dict)
     else:
         pass
     
reset_button.bind(on_press=total_reset)
add_button.bind(on_press=on_press_add_button)
selection_button.bind(on_release=dropdown.open)

DietCounterScreen.add_widget(mainlayout)

#FOODCOUNTERSCREEN
FoodCounterScreen = Screen(name='FoodCounter')

s2_reset_button = Button(background_normal='Fenix.jpg', background_down='Fenix.jpg', size_hint=(0.65,1), pos_hint={'center_x': .5, 'center_y': .5})
s2_calories_label = Label(text='0 ккал/г', font_size=300, font_name=teremokfont, pos_hint={'center_x': .5, 'center_y': .5}) # 
s2_selection_button = Button(text='Стандарт', background_color=(0,0,0,0), font_name=teremokfont, font_size=mainmenufontsize) #, size_hint=(0.5, 0.5)
s2_dropdown = DropDown()
s2_portion_input = TextInput(text='1', multiline=False, font_name=teremokfont, font_size=120, size_hint=(0.25, 0.5)) #background_color=(0,0,0,0), foreground_color=(1,1,1,1), 

foodcounterscreenlayout = BoxLayout(orientation='vertical')
foodcounterscreenlayout.add_widget(s2_portion_input)
foodcounterscreenlayout.add_widget(s2_reset_button)
foodcounterscreenlayout.add_widget(s2_calories_label)
foodcounterscreenlayout.add_widget(s2_selection_button)


numeric_keyboard_layout = FloatLayout()
numeric_keyboard_coords_x = [0, .1, .2, .3, .1, .2, .3, .1, .2, .3]
numeric_keyboard_coords_y = [0, .3, .3, .3, .2, .2, .2, .1, .1, .1]

# def on_key(instance):
#     s2_calories_label.text = instance.text
    
# for num in range(1,10):
#     globals()['button_'+str(num)] = Button(text=str(num), font_name=teremokfont, font_size=mainmenufontsize, size_hint=(.1, .1), pos_hint={'x':numeric_keyboard_coords_x[num], 'y':numeric_keyboard_coords_y[num]})
#     numeric_keyboard_layout.add_widget(globals()['button_'+str(num)])
#     globals()['button_'+str(num)].bind(on_press=on_key)
               
def s2_dropdownmenu(dictionary, *args):
     
    s2_dropdown.clear_widgets()
     
    for key in dictionary:
        btn = Button(text=key, background_color=(0,0,0,1), font_name=teremokfont, font_size=mainmenufontsize, size_hint_y=None) #, height=120
        btn.bind(on_release=lambda btn: s2_dropdown.select(btn.text))
        s2_dropdown.add_widget(btn)            

s2_dropdownmenu(food_dict)

# class MyKeyboardListener(Widget):

#     def __init__(self, **kwargs):
#         super(MyKeyboardListener, self).__init__(**kwargs)
#         self._keyboard = Window.request_keyboard(
#             self._keyboard_closed, self, 'text')
#         if self._keyboard.widget:
#             vkeyboard = self._keyboard.widget
#             vkeyboard.layout = 'numeric.json'
#             #pass
#         self._keyboard.bind(on_key_down=self._on_keyboard_down)

#     def _keyboard_closed(self):
#         print('My keyboard have been closed!')
#         self._keyboard.unbind(on_key_down=self._on_keyboard_down)
#         self._keyboard = None

#     def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
#         print('The key', keycode, 'have been pressed')
#         print(' - text is %r' % text)
#         print(' - modifiers are %r' % modifiers)

#         # Keycode is composed of an integer + a string
#         # If we hit escape, release the keyboard
#         if keycode[1] == 'escape':
#             keyboard.release()

#         # Return True to accept the key. Otherwise, it will be used by
#         # the system.
#         return True


    
    
def on_key_a(*args):
    # for key,value in food_dict.items():
    #     if keycode[1] == key[0]:
    #         food_sorter[key]=value
    #     else:
    #         pass
    
    # s2_dropdownmenu(food_sorter)
    # print(keycode)
    # print(keyboard)
    # s2_calories_label.text = str(text)
    s2_calories_label.text = s2_portion_input.text[-1]
    
    # if keycode[1] == 'ф':
    #     s2_calories_label.text = keycode[1]
    #     keyboard.release()
    
def dropsearch(instance):
    s2_dropdown.open(s2_selection_button)
    # FoodCounterScreen.add_widget(numeric_keyboard_layout)
    # VKeyboard().bind(on_key_down=on_key_a)
    # return Window.request_keyboard(None, s2_selection_button).widget
    # vkeyboard.layout = 'numeric.json'
    
    # Window.request_keyboard(None, s2_selection_button).bind(on_key_down=on_key_a)
    Window.request_keyboard(None, s2_portion_input)
    Window.on_key_up = on_key_a

s2_selection_button.bind(on_release=dropsearch)
s2_dropdown.bind(on_select=lambda instance, x: setattr(s2_selection_button, 'text', x))

FoodCounterScreen.add_widget(foodcounterscreenlayout)


carousel = Carousel(direction='right')
carousel.add_widget(DietCounterScreen)
carousel.add_widget(FoodCounterScreen)

class MainApp(App):
    def build(self):
        return carousel
    
    
if __name__ == '__main__':
    MainApp().run()