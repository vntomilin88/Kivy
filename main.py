# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 00:48:54 2020

@author: vntom
"""

#from kivy.config import Config
# Config.set('kivy', 'default_font', ["Arial", "C:/Windows/Fonts/arial.ttf", "C:/Windows/Fonts/ariali.ttf", "C:/Windows/Fonts/arialbd.ttf", "C:/Windows/Fonts/arialbi.ttf"])
#Config.set('kivy', 'default_font', ['Izhitsa', 'Izhitsa.ttf'])
#Config.write() 
import csv

from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.uix.carousel import Carousel
from kivy.uix.dropdown import DropDown
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen

dish_weight = 0
mainmenufontsize = 120
teremokfont = 'Teremok'
 
LabelBase.register(name='Teremok', fn_regular='Teremok.ttf') #, fn_bold=''
everyday_food_dict = {x[0]:x[1:] for x in list(csv.reader(open('Databases/Everyday.csv', encoding='utf-8')))} #создаём словарь из первого элемента листа .csv фаила как ключа, и остальных элементов как значения, используя словарное сокращение
ingredients_dict = {x[0]:x[1:] for x in list(csv.reader(open('Databases/Ingredients.csv', encoding='utf-8')))}


#Functions
def dropdownmenu(food_sorter, food_menu):
     
    food_menu.clear_widgets()
     
    for key in food_sorter:
        btn = Button(text=key, background_color=(0,0,0,1), font_name=teremokfont, font_size=110, size_hint_y=None) #, height=120
        btn.bind(on_release=lambda btn: food_menu.select(btn.text))
        food_menu.add_widget(btn)

def on_key(food_sorter, food_dict, search_input, food_menu, x):
    print(x)
    food_sorter = {}
    for key,value in food_dict.items():
        if key[0] == str(x[-1].upper()): #search_input.text
            food_sorter[key]=value
        else:
            pass
    
    dropdownmenu(food_sorter, food_menu)
    search_input.text = x[-1]
    
def dropsearch(food_menu, selection_button, search_input, food_sorter, food_dict):
    food_menu.open(selection_button)
    Window.request_keyboard(None, selection_button)
    search_input.focus = True
    search_input.bind(text=lambda instance, x: on_key(food_sorter, food_dict, search_input, food_menu, x))


def dropdownbind(x, selection_button, portion_input):
    setattr(selection_button, 'text', x) #setattr(object, name, value) - sets value of an attribute of an object
    Window.request_keyboard(None, selection_button)
    portion_input.focus = True

def addition(caloriecount, log_text_file, log, selection_button, portion_input, food_dict, calories_label, total_weight_label, calories_per_g_label, protein_label, fat_label, carb_label, search_input, food_menu, kkal):
    if portion_input.text.isdigit() == True:
        calories_label.text = str(round(float(calories_label.text.split()[0]) + float(portion_input.text)*float(food_dict[selection_button.text][0])))+ kkal
        total_weight_label.text = str(float(total_weight_label.text.split()[0]) + float(portion_input.text))+' г' 
        calories_per_g_label.text = str(round(float(calories_label.text.split()[0])/float(total_weight_label.text.split()[0]),2))+' ккал/г'
        protein_label.text = str(round(float(protein_label.text.split()[0]) + float(portion_input.text)*float(food_dict[selection_button.text][1])))+' белков'
        fat_label.text = str(round(float(fat_label.text.split()[0]) + float(portion_input.text)*float(food_dict[selection_button.text][2])))+' жиров'
        carb_label.text = str(round(float(carb_label.text.split()[0]) + float(portion_input.text)*float(food_dict[selection_button.text][3])))+' углеводов'
        open(caloriecount, mode='w+', encoding='utf-8').write(f'{calories_label.text.split()[0]}\n{total_weight_label.text.split()[0]} г\n{calories_per_g_label.text.split()[0]} ккал/г\n{protein_label.text.split()[0]} белков\n{fat_label.text.split()[0]} жиров\n{carb_label.text.split()[0]} углеводов')
        open(log_text_file, mode='a', encoding='utf-8').write(f'{portion_input.text}г/шт {selection_button.text}: {str(round(float(portion_input.text)*float(food_dict[selection_button.text][0])))}ккал\n') #f'{log.text}{portion_input.text}г/шт {selection_button.text}: {str(round(float(portion_input.text)*float(food_dict[selection_button.text][0])))}ккал\n'
        log.text = open(log_text_file, encoding='utf-8').read()
        portion_input.text = ''
        dropdownmenu(food_dict, food_menu)
    else:
         pass
     
def log_clear(caloriecount, log_text_file, log, calories_label, total_weight_label, calories_per_g_label, protein_label, fat_label, carb_label):
    open(log_text_file, mode='w', encoding='utf-8')
    log.text = ''
    open(caloriecount, mode='w+', encoding='utf-8').write('0\n0 г\n0 ккал/г\n0 белков\n0 жиров\n0 углеводов')
    [calories_label.text, total_weight_label.text, calories_per_g_label.text, protein_label.text, fat_label.text, carb_label.text] = ['0', '0 г', '0 ккал/г', '0 белков', '0 жиров', '0 углеводов']
    
    
#DIETCOUNTERSCREEN (Screen 1 - s1)
food_sorter_s1 = {}

DietCounterScreen = Screen(name='DietCounter')

#Elements s1
log_button_s1 = Button(background_normal='Fenix.jpg', background_down='Fenix.jpg', size_hint=(0.65,1), pos_hint={'center_x': .5, 'center_y': .5})
calories_label_s1 = Label(text=open('Databases/caloriecount_s1.txt', mode='r', encoding='utf-8').readlines()[0], font_name=teremokfont, font_size=270, pos_hint={'center_x': .5, 'center_y': .5}) #size_hint=(None, None), bold=False, 
calories_text_label_s1 = Label(text='ккал', font_name=teremokfont, font_size=200, pos_hint={'center_x': .5, 'center_y': .5}) #size_hint=(None, None),
total_weight_label_s1 = Label(text=open('Databases/caloriecount_s1.txt', mode='r', encoding='utf-8').readlines()[1], font_size=270, font_name=teremokfont, pos_hint={'center_x': .5, 'center_y': .5})
calories_per_g_label_s1 = Label(text=open('Databases/caloriecount_s1.txt', mode='r', encoding='utf-8').readlines()[2], font_size=270, font_name=teremokfont, pos_hint={'center_x': .5, 'center_y': .5})
protein_label_s1 = Label(text=open('Databases/caloriecount_s1.txt', mode='r', encoding='utf-8').readlines()[3], font_name=teremokfont, color=(1,1,1,1), font_size=80, pos_hint={'center_x': .5, 'center_y': .5})
fat_label_s1 = Label(text=open('Databases/caloriecount_s1.txt', mode='r', encoding='utf-8').readlines()[4], font_name=teremokfont, color=(1,0.874,0,1),  font_size=80, pos_hint={'center_x': .5, 'center_y': .5})
carb_label_s1 = Label(text=open('Databases/caloriecount_s1.txt', mode='r', encoding='utf-8').readlines()[5], font_name=teremokfont, color=(0.65,0,0.12,1), font_size=80, pos_hint={'center_x': .5, 'center_y': .5})

search_input_s1 = TextInput(text='', font_name=teremokfont, foreground_color=(1,1,1,1), background_color=(0,0,0,0), multiline=False, font_size=120, size_hint=(0.125, 0.5))

selection_button_s1 = Button(text='Стандарт', background_color=(0,0,0,0), font_name=teremokfont, font_size=mainmenufontsize, size_hint=(0.5, 0.5)) #
food_menu_s1 = DropDown()

portion_input_s1 = TextInput(multiline=False, background_color=(0,0,0,0), font_name=teremokfont,  foreground_color=(1,1,1,1), font_size=mainmenufontsize, size_hint=(0.25, 0.37)) 

add_button_s1 = Button(text='+', background_color=(0,0,0,0), font_name=teremokfont, font_size=mainmenufontsize, size_hint=(0.125, 0.5)) #, size_hint=(None, None)
        
calories_base_label_s1 = Label(text='',font_name=teremokfont, color=(1,1,1,0.6),  font_size=200, pos_hint={'center_x': .5, 'center_y': .5})
calories_text1_label_s1 = Label(text='', font_name=teremokfont, color=(1,1,1,0.6),  font_size=100, pos_hint={'center_x': .5, 'center_y': .5})
protein_base_label_s1 = Label(text='', font_name=teremokfont, color=(1,1,1,0.6),  font_size=70) #, pos_hint={'center_x': .5, 'center_y': .5}
fat_base_label_s1 = Label(text='', font_name=teremokfont, color=(1,0.874,0,0.6),  font_size=70) #, pos_hint={'center_x': .5, 'center_y': .5}
carb_base_label_s1 = Label(text='', font_name=teremokfont, color=(0.65,0,0.12,0.6),  font_size=70) #, pos_hint={'center_x': .5, 'center_y': .5}

spacer1_s1 = Label(text='Filler', font_name=teremokfont, color=(0,0,0,0), pos_hint={'center_x': .5, 'center_y': .5}) # [255,255,255,255]
spacer2_s1 = Label(text='Filler', font_name=teremokfont, color=(0,0,0,0), pos_hint={'center_x': .5, 'center_y': .5}) # [255,255,255,255]

    #Calorie Box
caloriebox_s1 = BoxLayout(padding=20, orientation='vertical')
#Calorie Elements
caloriebox_s1.add_widget(calories_label_s1)
caloriebox_s1.add_widget(calories_text_label_s1)
        
    #P/F/C Elements
   
#P/F/C Box
pfcbox_s1 = BoxLayout(padding=0, orientation='vertical')
pfcbox_s1.add_widget(protein_label_s1)
pfcbox_s1.add_widget(fat_label_s1)
pfcbox_s1.add_widget(carb_label_s1)

    #Row 2
row2_s1 = BoxLayout(padding=0, orientation='horizontal')
#Row 2 Elements
row2_s1.add_widget(caloriebox_s1)
row2_s1.add_widget(pfcbox_s1)

    #Row 3
row3_s1 = BoxLayout(padding=0, orientation='horizontal')
#Row 3 Elements
#row3_s1.add_widget(search_input_s1)
row3_s1.add_widget(selection_button_s1)
row3_s1.add_widget(portion_input_s1)
row3_s1.add_widget(add_button_s1)

#Calorie_base Box
caloriebasebox_s1 = BoxLayout(padding=20, orientation='vertical')
#Calorie Elements
caloriebasebox_s1.add_widget(calories_base_label_s1)
caloriebasebox_s1.add_widget(calories_text1_label_s1)

#P/F/C_base Box
pfcbasebox_s1 = BoxLayout(padding=0, orientation='vertical')
#P/F/C_base Elements
pfcbasebox_s1.add_widget(protein_base_label_s1)
pfcbasebox_s1.add_widget(fat_base_label_s1)
pfcbasebox_s1.add_widget(carb_base_label_s1)

    #Row 4
row4_s1 = BoxLayout(padding=0, orientation='horizontal')
row4_s1.add_widget(caloriebasebox_s1)
row4_s1.add_widget(pfcbasebox_s1)

    #Row 5
row5_s1 = BoxLayout(padding=0, orientation='horizontal')
row5_s1.add_widget(spacer1_s1)
 
   #Row 6
row6_s1 = BoxLayout(padding=0, orientation='horizontal')
row6_s1.add_widget(spacer2_s1)

    #Main Layout
dietcounterscreenlayout = BoxLayout(padding=0, orientation='vertical')
#Main Elements
dietcounterscreenlayout.add_widget(log_button_s1) #Row 1
dietcounterscreenlayout.add_widget(row2_s1)
dietcounterscreenlayout.add_widget(row3_s1)
dietcounterscreenlayout.add_widget(row4_s1)
dietcounterscreenlayout.add_widget(row5_s1)

DietCounterScreen.add_widget(dietcounterscreenlayout)

#Local Functions
def base(instance, x, food_dict):
    if x == '':
        calories_base_label_s1.text = ''
        calories_text1_label_s1.text = ''
        protein_base_label_s1.text = ''
        fat_base_label_s1.text = ''
        carb_base_label_s1.text = ''
    else:    
        calories_base_label_s1.text = str(round((float(x)*float(food_dict[selection_button_s1.text][0]))))
        calories_text1_label_s1.text = 'ккал'
        protein_base_label_s1.text = str(round((float(x)*float(food_dict[selection_button_s1.text][1])))) +' белков'
        fat_base_label_s1.text = str(round((float(x)*float(food_dict[selection_button_s1.text][2])))) +' жиров'
        carb_base_label_s1.text = str(round((float(x)*float(food_dict[selection_button_s1.text][3])))) +' углеводов'

#POPUP S1
pp_s1_layout = BoxLayout(padding=0, orientation='vertical')
log_s1 = Label(text=open('Databases/log_s1.txt', encoding='utf-8').read(), font_name=teremokfont, font_size=90, pos_hint={'center_x': .5, 'center_y': .5})
log_s1_reset_button = Button(text='Отчистить', background_color=(0,0,0,0), font_name=teremokfont, font_size=mainmenufontsize)

pp_s1_layout.add_widget(log_s1)
pp_s1_layout.add_widget(log_s1_reset_button) #, size_hint=(0.5, 0.5)

popup_log_s1 = Popup(title='~ Откушано ~', title_font=teremokfont, title_size=160, title_align='center', separator_color=(1,1,1,1), background_color=(0,0,0,0.75), content=pp_s1_layout, size_hint=(0.9, 0.9)) #, size=(400, 400)

log_s1_reset_button.bind(on_release=lambda instance: log_clear('Databases/caloriecount_s1.txt', 'Databases/log_s1.txt', log_s1, calories_label_s1, total_weight_label_s1, calories_per_g_label_s1, protein_label_s1, fat_label_s1, carb_label_s1))

#Logic
log_button_s1.bind(on_release=popup_log_s1.open)
dropdownmenu(everyday_food_dict, food_menu_s1)
selection_button_s1.bind(on_release=lambda instance: dropsearch(food_menu_s1, selection_button_s1, search_input_s1, food_sorter_s1, everyday_food_dict))
food_menu_s1.bind(on_select=lambda instance, x: dropdownbind(x, selection_button_s1, portion_input_s1))
portion_input_s1.bind(text=lambda instance, x: base(instance, x, everyday_food_dict), 
                      on_text_validate=lambda instance: addition('Databases/caloriecount_s1.txt', 'Databases/log_s1.txt', log_s1, selection_button_s1, portion_input_s1, everyday_food_dict, calories_label_s1, total_weight_label_s1, calories_per_g_label_s1, protein_label_s1, fat_label_s1, carb_label_s1, search_input_s1, food_menu_s1, '',))
add_button_s1.bind(on_press=lambda instance: addition('Databases/caloriecount_s1.txt', 'Databases/log_s1.txt', log_s1, selection_button_s1, portion_input_s1, everyday_food_dict, calories_label_s1, total_weight_label_s1, calories_per_g_label_s1, protein_label_s1, fat_label_s1, carb_label_s1, search_input_s1, food_menu_s1, '',))

#FOODCOUNTERSCREEN (Screen 2 - s2)
food_sorter_s2 = {}

FoodCounterScreen = Screen(name='FoodCounter')

#Elements s2
log_s2 = Label(text='', font_name=teremokfont, font_size=90, pos_hint={'center_x': .5, 'center_y': .5})
log_button_s2 = Button(background_normal='Fenix.jpg', background_down='Fenix.jpg', size_hint=(0.65,1), pos_hint={'center_x': .5, 'center_y': .5})
calories_label_s2 = Label(text=open('Databases/caloriecount_s2.txt', mode='r', encoding='utf-8').readlines()[0], font_size=270, font_name=teremokfont, pos_hint={'center_x': .5, 'center_y': .5}) # 
total_weight_label_s2 = Label(text=open('Databases/caloriecount_s2.txt', mode='r', encoding='utf-8').readlines()[1], font_size=270, font_name=teremokfont, pos_hint={'center_x': .5, 'center_y': .5})
calories_per_g_label_s2 = Label(text=open('Databases/caloriecount_s2.txt', mode='r', encoding='utf-8').readlines()[2], font_size=270, font_name=teremokfont, pos_hint={'center_x': .5, 'center_y': .5}, size_hint=(0.75, 1))
protein_label_s2 = Label(text=open('Databases/caloriecount_s2.txt', mode='r', encoding='utf-8').readlines()[3], font_name=teremokfont, color=(1,1,1,1), font_size=80, pos_hint={'center_x': .5, 'center_y': .5})
fat_label_s2 = Label(text=open('Databases/caloriecount_s2.txt', mode='r', encoding='utf-8').readlines()[4], font_name=teremokfont, color=(1,0.874,0,1),  font_size=80, pos_hint={'center_x': .5, 'center_y': .5})
carb_label_s2 = Label(text=open('Databases/caloriecount_s2.txt', mode='r', encoding='utf-8').readlines()[5], font_name=teremokfont, color=(0.65,0,0.12,1), font_size=80, pos_hint={'center_x': .5, 'center_y': .5})
search_input_s2 = TextInput(text='', multiline=False, font_name=teremokfont, font_size=120, size_hint=(0.25, 0.5)) #background_color=(0,0,0,0), foreground_color=(1,1,1,1),
selection_button_s2 = Button(text='Стандарт', background_color=(0,0,0,0), font_name=teremokfont, font_size=mainmenufontsize, size_hint=(0.5, 0.5)) #
food_menu_s2 = DropDown()
portion_input_s2 = TextInput(multiline=False, background_color=(0,0,0,0), font_name=teremokfont,  foreground_color=(1,1,1,1), font_size=mainmenufontsize, size_hint=(0.25, 0.45))  
add_button_s2 = Button(text='+', background_color=(0,0,0,0), font_name=teremokfont, font_size=mainmenufontsize, size_hint=(0.125, 0.5))
final_weight_input_s2 = TextInput(multiline=False, font_name=teremokfont,  font_size=120, size_hint=(0.5, 0.25), pos_hint={'center_x': .5, 'center_y': .5}) #background_color=(0,0,0,0), foreground_color=(1,1,1,1),  
spacer1_s2 = Label(text='Filler', font_name=teremokfont, color=(0,0,0,0), pos_hint={'center_x': .5, 'center_y': .5})
spacer2_s2 = Label(text='Filler', font_name=teremokfont, color=(0,0,0,0), pos_hint={'center_x': .5, 'center_y': .5})
spacer3_s2 = Label(text='Filler', font_name=teremokfont, color=(0,0,0,0), pos_hint={'center_x': .5, 'center_y': .5})

    #Row 3
row3_s2 = BoxLayout(padding=0, orientation='horizontal')
#Row 3 Elements
#row3_s1.add_widget(search_input_s1)
row3_s2.add_widget(selection_button_s2)
row3_s2.add_widget(portion_input_s2)
row3_s2.add_widget(add_button_s2)

#Row 5
row5_s2 = BoxLayout(padding=0, orientation='horizontal')
row5_s2.add_widget(spacer1_s2)
# row5_s2.add_widget(total_weight_label_s2)
# row5_s2.add_widget(calories_per_g_label_s2)

#Row 6
row6_s2 = BoxLayout(padding=0, orientation='horizontal')
row6_s2.add_widget(spacer2_s2)

#Row 7
row7_s2 = BoxLayout(padding=0, orientation='horizontal')
row7_s2.add_widget(spacer3_s2)

foodcounterscreenlayout = BoxLayout(orientation='vertical')
foodcounterscreenlayout.add_widget(log_button_s2) #Row 1
foodcounterscreenlayout.add_widget(calories_per_g_label_s2) #Row 2
foodcounterscreenlayout.add_widget(row3_s2)
foodcounterscreenlayout.add_widget(final_weight_input_s2) #Row 4
foodcounterscreenlayout.add_widget(row5_s2)
foodcounterscreenlayout.add_widget(row6_s2)
foodcounterscreenlayout.add_widget(row7_s2)

FoodCounterScreen.add_widget(foodcounterscreenlayout)

#POPUP S2
pp_s2_layout = BoxLayout(padding=0, orientation='vertical')
log_s2 = Label(text=open('Databases/log_s2.txt', encoding='utf-8').read(), font_name=teremokfont, font_size=90, pos_hint={'center_x': .5, 'center_y': .5})
log_s2_reset_button = Button(text='Отчистить', background_color=(0,0,0,0), font_name=teremokfont, font_size=mainmenufontsize)

pp_s2_layout.add_widget(log_s2)
pp_s2_layout.add_widget(log_s2_reset_button) #, size_hint=(0.5, 0.5)

popup_log_s2 = Popup(title='~ Добавлено ~', title_font=teremokfont, title_size=160, title_align='center', separator_color=(1,1,1,1), background_color=(0,0,0,0.75), content=pp_s2_layout, size_hint=(0.9, 0.9)) #, size=(400, 400)

log_s2_reset_button.bind(on_release=lambda instance: log_clear('Databases/caloriecount_s2.txt', 'Databases/log_s2.txt', log_s2, calories_label_s2, total_weight_label_s2, calories_per_g_label_s2, protein_label_s2, fat_label_s2, carb_label_s2))

#Logic
log_button_s2.bind(on_release=popup_log_s2.open)
dropdownmenu(ingredients_dict, food_menu_s2)
selection_button_s2.bind(on_release=lambda instance: dropsearch(food_menu_s2, selection_button_s2, search_input_s2, food_sorter_s2, ingredients_dict))
food_menu_s2.bind(on_select=lambda instance, x: dropdownbind(x, selection_button_s2, portion_input_s2))
portion_input_s2.bind(on_text_validate=lambda instance: addition('Databases/caloriecount_s2.txt', 'Databases/log_s2.txt', log_s2, selection_button_s2, portion_input_s2, ingredients_dict, calories_label_s2, total_weight_label_s2, calories_per_g_label_s2, protein_label_s2, fat_label_s2, carb_label_s2, search_input_s2, food_menu_s2, ' ккал',))
add_button_s2.bind(on_press=lambda instance: addition('Databases/caloriecount_s2.txt', 'Databases/log_s2.txt', log_s2, selection_button_s2, portion_input_s2, ingredients_dict, calories_label_s2, total_weight_label_s2, calories_per_g_label_s2, protein_label_s2, fat_label_s2, carb_label_s2, search_input_s2, food_menu_s2, ' ккал',))
final_weight_input_s2.bind(on_text_validate=lambda instance: setattr(calories_per_g_label_s2, 'text', str(round(float(calories_label_s2.text.split()[0])/float(final_weight_input_s2.text),2))))


#Screen Carousel
carousel = Carousel(direction='right')
carousel.add_widget(DietCounterScreen)
carousel.add_widget(FoodCounterScreen)

class MainApp(App):
    def build(self):
        return carousel
    
if __name__ == '__main__':
    MainApp().run()