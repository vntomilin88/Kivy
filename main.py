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

#from android.storage import primary_external_storage_path
#from android.permissions import request_permissions, Permission

#request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])

#SD_CARD = primary_external_storage_path()

dish_weight = 0
mainmenufontsize = 120
teremokfont = 'Teremok'
local_path = 'Databases/'
android_path = '/sdcard/Android/media/com.nextcloud.client/nextcloud/vntomilin88@oblaco.ddns.net%2Fnextcloud/Prima-Terra/Scripts/Calorie Counter App/Databases/'
# the_path = android_path
the_path = local_path

LabelBase.register(name='Teremok', fn_regular='Teremok.ttf') #, fn_bold=''

everyday_food_dict = {x[0]:x[1:] for x in list(csv.reader(open(the_path + 'Everyday.csv', encoding='utf-8')))} #создаём словарь из первого элемента листа .csv фаила как ключа, и остальных элементов как значения, используя словарное сокращение
ingredients_dict = {x[0]:x[1:] for x in list(csv.reader(open(the_path + 'Ingredients.csv', encoding='utf-8')))}
recipe_dict = {x[0]:x[1:] for x in list(csv.reader(open(the_path + 'Recipes.csv', encoding='utf-8')))}
#print(list(csv.reader(open(the_path + 'Recipes.csv', encoding='utf-8'))))

button_list = []

#Functions
def dropdownmenu(food_sorter, food_menu):
    
    for btn in button_list:
        food_menu.remove_widget(btn)
        
    for key in food_sorter:
        btn = Button(text=key, background_color=(0,0,0,1), font_name=teremokfont, font_size=110, size_hint_y=None) #, height=120
        btn.bind(on_release=lambda btn: food_menu.select(btn.text))
        button_list.append(btn)
        food_menu.add_widget(btn)

def on_key(food_sorter, food_dict, search_input, food_menu, x):
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

def dropdownbind(x, selection_button, portion_input, recipe):
    setattr(selection_button, 'text', x) #setattr(object, name, value) - sets value of an attribute of an object
    Window.request_keyboard(None, selection_button)
    portion_input.focus = True
    try:
        recipe.text = ''
        for component in recipe_dict[selection_button.text]:
            recipe.text += f'{component}\n'
    except:
        pass


def addition(caloriecount, log_text_file, log, selection_button, portion_input, food_dict, calories_label, total_weight_label, calories_per_g_label, protein_label, fat_label, carb_label, search_input, food_menu, kkal):
    if portion_input.text.isdigit() == True:
        calories_label.text = str(round(float(calories_label.text.split()[0]) + float(portion_input.text)*float(food_dict[selection_button.text][0])))+ kkal
        total_weight_label.text = str(float(total_weight_label.text.split()[0]) + float(portion_input.text))+' г' 
        calories_per_g_label.text = str(round(float(calories_label.text.split()[0])/float(total_weight_label.text.split()[0]),2))+' ккал/г'
        protein_label.text = str(round(float(protein_label.text.split()[0]) + float(portion_input.text)*float(food_dict[selection_button.text][1])))+' белков'
        fat_label.text = str(round(float(fat_label.text.split()[0]) + float(portion_input.text)*float(food_dict[selection_button.text][2])))+' жиров'
        carb_label.text = str(round(float(carb_label.text.split()[0]) + float(portion_input.text)*float(food_dict[selection_button.text][3])))+' углеводов'
        open(caloriecount, mode='w+', encoding='utf-8').write(f'{calories_label.text.split()[0]} ккал\n{total_weight_label.text.split()[0]} г\n{calories_per_g_label.text.split()[0]} ккал/г\n{protein_label.text.split()[0]} белков\n{fat_label.text.split()[0]} жиров\n{carb_label.text.split()[0]} углеводов')
        open(log_text_file, mode='a', encoding='utf-8').write(f'{portion_input.text}г/шт {selection_button.text}: {str(round(float(portion_input.text)*float(food_dict[selection_button.text][0])))}ккал\n') #f'{log.text}{portion_input.text}г/шт {selection_button.text}: {str(round(float(portion_input.text)*float(food_dict[selection_button.text][0])))}ккал\n'
        log.text = open(log_text_file, encoding='utf-8').read()
        portion_input.text = ''
        dropdownmenu(food_dict, food_menu)
        
        if log_text_file == str(the_path + 'log_s1.txt'):
           calorie_label_s0.text = calories_label.text
        else:
            pass
    
    else:
         pass
     
def log_clear(caloriecount, log_text_file, log, calories_label, total_weight_label, calories_per_g_label, protein_label, fat_label, carb_label):
    open(log_text_file, mode='w', encoding='utf-8')
    log.text = ''
    open(caloriecount, mode='w+', encoding='utf-8').write('0 ккал\n0 г\n0 ккал/г\n0 белков\n0 жиров\n0 углеводов')
    [calories_label.text, total_weight_label.text, calories_per_g_label.text, protein_label.text, fat_label.text, carb_label.text] = ['0', '0 г', '0 ккал/г', '0 белков', '0 жиров', '0 углеводов']

def food_add(dish_name, final_weight, calories, proteins, fats, carbs):
    dish_is_not_present = True
    food_list = []
    
    for food in list(csv.reader(open(the_path + 'Everyday.csv', encoding='utf-8'))):
        
        if dish_name in food:
            dish_is_not_present = False
            food = [dish_name.text,round(float(calories.text)/float(final_weight.text),2),round(float(proteins.text)/float(final_weight.text),2),round(float(fats.text)/float(final_weight.text),2),round(float(carbs.text)/float(final_weight.text),2)]
            food_list.append(food)
        else:
            food_list.append(food)
    
    csv.writer(open(the_path + 'Everyday.csv', 'w', newline='', encoding='utf-8'), delimiter=',').writerows(food_list)
          
    if dish_is_not_present:
        csv.writer(open(the_path + 'Everyday.csv', 'a+', newline='', encoding='utf-8'), delimiter=',').writerow([dish_name.text,round(float(calories.text)/float(final_weight.text),2),round(float(proteins.text)/float(final_weight.text),2),round(float(fats.text)/float(final_weight.text),2),round(float(carbs.text)/float(final_weight.text),2)])
    
    [dish_name.text, final_weight.text, calories.text, proteins.text, fats.text, carbs.text] = ['', '', '', '', '', '',]
    
#MAINSCREEN (Screen 0 - s0)
MainScreen = Screen(name='Main')

#Elements s0
submit_button_s0 = Button(background_normal='Fenix.jpg', background_down='Fenix.jpg', size_hint=(0.65,1), pos_hint={'center_x': .5, 'center_y': .5})
calorie_label_s0 = Label(text=open(the_path + 'caloriecount_s1.txt', mode='r', encoding='utf-8').readlines()[0], font_name=teremokfont, font_size=270, pos_hint={'center_x': .5, 'center_y': .5})
log_label_s0 = Label(text=open(the_path + 'log_s1.txt', encoding='utf-8').read(), font_name=teremokfont, font_size=90, pos_hint={'center_x': .5, 'center_y': .5}) #open(the_path + 'log_s1.txt', encoding='utf-8').read()
log_reset_button_s0 = Button(text='Отчистить', background_color=(0,0,0,0), font_name=teremokfont, font_size=mainmenufontsize)

mainscreenlayout = BoxLayout(orientation='vertical')
mainscreenlayout.add_widget(submit_button_s0)
mainscreenlayout.add_widget(calorie_label_s0)
mainscreenlayout.add_widget(log_label_s0)
mainscreenlayout.add_widget(log_reset_button_s0)

MainScreen.add_widget(mainscreenlayout)

#Logic
log_reset_button_s0.bind(on_release=lambda instance: log_clear(the_path + 'caloriecount_s1.txt', the_path + 'log_s1.txt', log_label_s0, calories_label_s1, total_weight_label_s1, calories_per_g_label_s1, protein_label_s1, fat_label_s1, carb_label_s1))

#DIETCOUNTERSCREEN (Screen 1 - s1)
food_sorter_s1 = {}

DietCounterScreen = Screen(name='DietCounter')

#Elements s1
log_button_s1 = Button(background_normal='Fenix.jpg', background_down='Fenix.jpg', size_hint=(0.65,1), pos_hint={'center_x': .5, 'center_y': .5})
calories_label_s1 = Label(text=open(the_path + 'caloriecount_s1.txt', mode='r', encoding='utf-8').readlines()[0], font_name=teremokfont, font_size=270, pos_hint={'center_x': .5, 'center_y': .5}) #size_hint=(None, None), bold=False, 
calories_text_label_s1 = Label(text='', font_name=teremokfont, font_size=200, pos_hint={'center_x': .5, 'center_y': .5}) #size_hint=(None, None),
total_weight_label_s1 = Label(text=open(the_path + 'caloriecount_s1.txt', mode='r', encoding='utf-8').readlines()[1], font_size=270, font_name=teremokfont, pos_hint={'center_x': .5, 'center_y': .5})
calories_per_g_label_s1 = Label(text=open(the_path + 'caloriecount_s1.txt', mode='r', encoding='utf-8').readlines()[2], font_size=270, font_name=teremokfont, pos_hint={'center_x': .5, 'center_y': .5})
protein_label_s1 = Label(text=open(the_path + 'caloriecount_s1.txt', mode='r', encoding='utf-8').readlines()[3], font_name=teremokfont, color=(1,1,1,1), font_size=80, pos_hint={'center_x': .5, 'center_y': .5})
fat_label_s1 = Label(text=open(the_path + 'caloriecount_s1.txt', mode='r', encoding='utf-8').readlines()[4], font_name=teremokfont, color=(1,0.874,0,1),  font_size=80, pos_hint={'center_x': .5, 'center_y': .5})
carb_label_s1 = Label(text=open(the_path + 'caloriecount_s1.txt', mode='r', encoding='utf-8').readlines()[5], font_name=teremokfont, color=(0.65,0,0.12,1), font_size=80, pos_hint={'center_x': .5, 'center_y': .5})

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
caloriebox_s1.add_widget(calories_base_label_s1)
caloriebox_s1.add_widget(calories_text1_label_s1)
        
    #P/F/C Elements
   
#P/F/C Box
pfcbox_s1 = BoxLayout(padding=0, orientation='vertical')
pfcbox_s1.add_widget(protein_base_label_s1)
pfcbox_s1.add_widget(fat_base_label_s1)
pfcbox_s1.add_widget(carb_base_label_s1)

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
caloriebasebox_s1.add_widget(calories_label_s1)
caloriebasebox_s1.add_widget(calories_text_label_s1)

#P/F/C_base Box
pfcbasebox_s1 = BoxLayout(padding=0, orientation='vertical')
#P/F/C_base Elements
pfcbasebox_s1.add_widget(protein_label_s1)
pfcbasebox_s1.add_widget(fat_label_s1)
pfcbasebox_s1.add_widget(carb_label_s1)

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
name_entry_label_pp_s1 = Label(text='Имья:', font_name=teremokfont, font_size=80, pos_hint={'center_x': .5, 'center_y': .5})
name_input_pp_s1 = TextInput(text='', multiline=False, font_name=teremokfont, font_size=120, pos_hint={'center_x': .1, 'center_y': .5}, size_hint=(0.7, 0.4))
kkal_entry_label_pp_s1 = Label(text='ккал:', font_name=teremokfont, font_size=80, pos_hint={'center_x': .5, 'center_y': .5})
kkal_input_pp_s1 = TextInput(text='', multiline=False, font_name=teremokfont, font_size=120, pos_hint={'center_x': .1, 'center_y': .5}, size_hint=(0.7, 0.4))
g_entry_label_pp_s1 = Label(text='грам/шт:', font_name=teremokfont, font_size=80, pos_hint={'center_x': .5, 'center_y': .5})
g_input_pp_s1 = TextInput(text='', multiline=False, font_name=teremokfont, font_size=120, pos_hint={'center_x': .1, 'center_y': .5}, size_hint=(0.7, 0.4))
protein_entry_label_pp_s1 = Label(text='Белков:', font_name=teremokfont, color=(1,1,1,1), font_size=80, pos_hint={'center_x': .5, 'center_y': .5})
protein_input_pp_s1 = TextInput(text='', multiline=False, font_name=teremokfont, font_size=120, pos_hint={'center_x': .1, 'center_y': .5}, size_hint=(0.7, 0.4))
fat_entry_label_pp_s1 = Label(text='Жиров:', font_name=teremokfont, color=(1,0.874,0,1), font_size=80, pos_hint={'center_x': .5, 'center_y': .5})
fat_input_pp_s1 = TextInput(text='', multiline=False, font_name=teremokfont, font_size=120, pos_hint={'center_x': .1, 'center_y': .5}, size_hint=(0.7, 0.4))
carb_entry_label_pp_s1 = Label(text='Углеводов:', font_name=teremokfont, color=(0.65,0,0.12,1), font_size=80, pos_hint={'center_x': .5, 'center_y': .5})
carb_input_pp_s1 = TextInput(text='', multiline=False, font_name=teremokfont, font_size=120, pos_hint={'center_x': .1, 'center_y': .5}, size_hint=(0.7, 0.4))
food_add_s1_button = Button(text='Добавить', background_color=(0,0,0,0), font_name=teremokfont, font_size=mainmenufontsize)

pp_s1_row0_layout = BoxLayout(padding=0, orientation='horizontal')
pp_s1_row0_layout.add_widget(name_entry_label_pp_s1)
pp_s1_row0_layout.add_widget(name_input_pp_s1)

pp_s1_row1_layout = BoxLayout(padding=0, orientation='horizontal')
pp_s1_row1_layout.add_widget(kkal_entry_label_pp_s1)
pp_s1_row1_layout.add_widget(kkal_input_pp_s1)

pp_s1_row2_layout = BoxLayout(padding=0, orientation='horizontal')
pp_s1_row2_layout.add_widget(g_entry_label_pp_s1)
pp_s1_row2_layout.add_widget(g_input_pp_s1)

pp_s1_row3_layout = BoxLayout(padding=0, orientation='horizontal')
pp_s1_row3_layout.add_widget(protein_entry_label_pp_s1)
pp_s1_row3_layout.add_widget(protein_input_pp_s1)

pp_s1_row4_layout = BoxLayout(padding=0, orientation='horizontal')
pp_s1_row4_layout.add_widget(fat_entry_label_pp_s1)
pp_s1_row4_layout.add_widget(fat_input_pp_s1)

pp_s1_row5_layout = BoxLayout(padding=0, orientation='horizontal')
pp_s1_row5_layout.add_widget(carb_entry_label_pp_s1)
pp_s1_row5_layout.add_widget(carb_input_pp_s1)

    
pp_s1_main_layout = BoxLayout(padding=0, orientation='vertical')
pp_s1_main_layout.add_widget(pp_s1_row0_layout)
pp_s1_main_layout.add_widget(pp_s1_row1_layout)
pp_s1_main_layout.add_widget(pp_s1_row2_layout)
pp_s1_main_layout.add_widget(pp_s1_row3_layout)
pp_s1_main_layout.add_widget(pp_s1_row4_layout)
pp_s1_main_layout.add_widget(pp_s1_row5_layout)
pp_s1_main_layout.add_widget(food_add_s1_button)


popup_log_s1 = Popup(title='~ Добавить ежи ~', title_font=teremokfont, title_size=160, title_align='center', separator_color=(1,1,1,1), background_color=(0,0,0,0.75), content=pp_s1_main_layout, size_hint=(0.9, 0.9)) #, size=(400, 400)

food_add_s1_button.bind(on_release=lambda instance: food_add(name_input_pp_s1, g_input_pp_s1, kkal_input_pp_s1, protein_input_pp_s1, fat_input_pp_s1, carb_input_pp_s1))

#Logic
log_button_s1.bind(on_release=popup_log_s1.open)
dropdownmenu(everyday_food_dict, food_menu_s1)
selection_button_s1.bind(on_release=lambda instance: dropsearch(food_menu_s1, selection_button_s1, search_input_s1, food_sorter_s1, everyday_food_dict))
food_menu_s1.bind(on_select=lambda instance, x: dropdownbind(x, selection_button_s1, portion_input_s1, spacer1_s1))
portion_input_s1.bind(text=lambda instance, x: base(instance, x, everyday_food_dict), 
                      on_text_validate=lambda instance: addition(the_path + 'caloriecount_s1.txt', the_path + 'log_s1.txt', log_label_s0, selection_button_s1, portion_input_s1, everyday_food_dict, calories_label_s1, total_weight_label_s1, calories_per_g_label_s1, protein_label_s1, fat_label_s1, carb_label_s1, search_input_s1, food_menu_s1, ' ккал',))
add_button_s1.bind(on_press=lambda instance: addition(the_path + 'caloriecount_s1.txt', the_path + 'log_s1.txt', log_label_s0, selection_button_s1, portion_input_s1, everyday_food_dict, calories_label_s1, total_weight_label_s1, calories_per_g_label_s1, protein_label_s1, fat_label_s1, carb_label_s1, search_input_s1, food_menu_s1, ' ккал',))

#FOODCOUNTERSCREEN (Screen 2 - s2)
food_sorter_s2 = {}

FoodCounterScreen = Screen(name='FoodCounter')

#Elements s2
log_s2 = Label(text='', font_name=teremokfont, font_size=90, pos_hint={'center_x': .5, 'center_y': .5})
log_button_s2 = Button(background_normal='Fenix.jpg', background_down='Fenix.jpg', size_hint=(0.65,1), pos_hint={'center_x': .5, 'center_y': .5})
calories_label_s2 = Label(text=open(the_path + 'caloriecount_s2.txt', mode='r', encoding='utf-8').readlines()[0], font_size=270, font_name=teremokfont, pos_hint={'center_x': .5, 'center_y': .5}) # 
total_weight_label_s2 = Label(text=open(the_path + 'caloriecount_s2.txt', mode='r', encoding='utf-8').readlines()[1], font_size=270, font_name=teremokfont, pos_hint={'center_x': .5, 'center_y': .5})
calories_per_g_label_s2 = Label(text=open(the_path + 'caloriecount_s2.txt', mode='r', encoding='utf-8').readlines()[2], font_size=270, font_name=teremokfont, pos_hint={'center_x': .5, 'center_y': .5}, size_hint=(0.75, 1))
protein_label_s2 = Label(text=open(the_path + 'caloriecount_s2.txt', mode='r', encoding='utf-8').readlines()[3], font_name=teremokfont, color=(1,1,1,1), font_size=80, pos_hint={'center_x': .5, 'center_y': .5})
fat_label_s2 = Label(text=open(the_path + 'caloriecount_s2.txt', mode='r', encoding='utf-8').readlines()[4], font_name=teremokfont, color=(1,0.874,0,1),  font_size=80, pos_hint={'center_x': .5, 'center_y': .5})
carb_label_s2 = Label(text=open(the_path + 'caloriecount_s2.txt', mode='r', encoding='utf-8').readlines()[5], font_name=teremokfont, color=(0.65,0,0.12,1), font_size=80, pos_hint={'center_x': .5, 'center_y': .5})
search_input_s2 = TextInput(text='', multiline=False, font_name=teremokfont, font_size=120, size_hint=(0.25, 0.5)) #background_color=(0,0,0,0), foreground_color=(1,1,1,1),
selection_button_s2 = Button(text='Стандарт', background_color=(0,0,0,0), font_name=teremokfont, font_size=mainmenufontsize, size_hint=(0.5, 0.5)) #
food_menu_s2 = DropDown()
portion_input_s2 = TextInput(multiline=False, background_color=(0,0,0,0), font_name=teremokfont,  foreground_color=(1,1,1,1), font_size=mainmenufontsize, size_hint=(0.25, 0.45))  
add_button_s2 = Button(text='+', background_color=(0,0,0,0), font_name=teremokfont, font_size=mainmenufontsize, size_hint=(0.125, 0.5))
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
foodcounterscreenlayout.add_widget(row5_s2)
foodcounterscreenlayout.add_widget(row6_s2)
foodcounterscreenlayout.add_widget(row7_s2)

FoodCounterScreen.add_widget(foodcounterscreenlayout)

#Local Functions s2

def add_dish(dish_name, final_weight):
    dish_is_not_present = True
    food_list = []
    
    for food in list(csv.reader(open(the_path + 'Everyday.csv', encoding='utf-8'))):
        
        if dish_name in food:
            dish_is_not_present = False
            food = [dish_name,round(float(calories_label_s2.text.split()[0])/float(final_weight),2),round(float(protein_label_s2.text.split()[0])/float(final_weight),2),round(float(fat_label_s2.text.split()[0])/float(final_weight),2),round(float(carb_label_s2.text.split()[0])/float(final_weight),2)]
            food_list.append(food)
        else:
            food_list.append(food)
    
    csv.writer(open(the_path + 'Everyday.csv', 'w', newline='', encoding='utf-8'), delimiter=',').writerows(food_list)
          
    if dish_is_not_present:
        csv.writer(open(the_path + 'Everyday.csv', 'a+', newline='', encoding='utf-8'), delimiter=',').writerow([dish_name,round(float(calories_label_s2.text.split()[0])/float(final_weight),2),round(float(protein_label_s2.text.split()[0])/float(final_weight),2),round(float(fat_label_s2.text.split()[0])/float(final_weight),2),round(float(carb_label_s2.text.split()[0])/float(final_weight),2)])
        
#POPUP S2
pp_s2_layout = BoxLayout(padding=0, orientation='vertical')
log_s2_dish_name_label = Label(text='Имя кушанья:', font_name=teremokfont, font_size=90, pos_hint={'center_x': 0, 'center_y': .5}) #
log_s2_dish_name_input = TextInput(text='', multiline=False, font_name=teremokfont, font_size=120, pos_hint={'center_x': .1, 'center_y': .5}, size_hint=(0.7, 0.4)) #
log_s2_final_weight_label = Label(text='Пудов:', font_name=teremokfont, font_size=90, pos_hint={'center_x': 0, 'center_y': .5}) #
log_s2_final_weight_input = TextInput(text=str(round(float(total_weight_label_s2.text.split()[0]))), multiline=False, font_name=teremokfont,  font_size=120, pos_hint={'center_x': .1, 'center_y': .5}, size_hint=(0.7, 0.4)) #background_color=(0,0,0,0), foreground_color=(1,1,1,1),  
log_s2 = Label(text=open(the_path + 'log_s2.txt', encoding='utf-8').read(), font_name=teremokfont, font_size=90, pos_hint={'center_x': .5, 'center_y': .5})
log_s2_reset_button = Button(text='Почистить', background_color=(0,0,0,0), font_name=teremokfont, font_size=mainmenufontsize)
log_s2_add_button = Button(text='Прибавить', background_color=(0,0,0,0), color=(1,0.874,0,1), font_name=teremokfont, font_size=mainmenufontsize)

pp_s2_dish_name_layout = BoxLayout(padding=0, orientation='horizontal')
pp_s2_dish_name_layout.add_widget(log_s2_dish_name_label)
pp_s2_dish_name_layout.add_widget(log_s2_dish_name_input)

pp_s2_final_weight_layout = BoxLayout(padding=0, orientation='horizontal')
pp_s2_final_weight_layout.add_widget(log_s2_final_weight_label)
pp_s2_final_weight_layout.add_widget(log_s2_final_weight_input)

pp_s2_button_layout = BoxLayout(padding=0, orientation='horizontal')
pp_s2_button_layout.add_widget(log_s2_reset_button)
pp_s2_button_layout.add_widget(log_s2_add_button)

pp_s2_layout.add_widget(pp_s2_dish_name_layout)
pp_s2_layout.add_widget(pp_s2_final_weight_layout)
pp_s2_layout.add_widget(log_s2)
pp_s2_layout.add_widget(pp_s2_button_layout) #, size_hint=(0.5, 0.5)

popup_log_s2 = Popup(title='~ Состав ~', title_font=teremokfont, title_size=160, title_align='center', separator_color=(1,1,1,1), background_color=(0,0,0,0.75), content=pp_s2_layout, size_hint=(0.9, 0.9)) #, size=(400, 400)

#POPUP S2 Functions:
def total_weight_suggestion():
    log_s2_final_weight_input.text = str(round(float(total_weight_label_s2.text.split()[0])))
    popup_log_s2.open()

def clear_log_and_weight():
    log_clear(the_path + 'caloriecount_s2.txt', the_path + 'log_s2.txt', log_s2, calories_label_s2, total_weight_label_s2, calories_per_g_label_s2, protein_label_s2, fat_label_s2, carb_label_s2)
    log_s2_final_weight_input.text = ''
    
#POPUP S2 Executables:
log_s2_reset_button.bind(on_release=lambda instance: clear_log_and_weight())
# log_s2_add_button.bind(on_release=lambda instance: add_dish(log_s2_dish_name_input.text, float(log_s2_final_weight_input.text)))
log_s2_add_button.bind(on_release=lambda instance: food_add(log_s2_dish_name_input, log_s2_final_weight_input, )))

#Logic
log_button_s2.bind(on_release=lambda instanse: total_weight_suggestion())
dropdownmenu(ingredients_dict, food_menu_s2)
selection_button_s2.bind(on_release=lambda instance: dropsearch(food_menu_s2, selection_button_s2, search_input_s2, food_sorter_s2, ingredients_dict))
food_menu_s2.bind(on_select=lambda instance, x: dropdownbind(x, selection_button_s2, portion_input_s2, spacer1_s2))
portion_input_s2.bind(on_text_validate=lambda instance: addition(the_path + 'caloriecount_s2.txt', the_path + 'log_s2.txt', log_s2, selection_button_s2, portion_input_s2, ingredients_dict, calories_label_s2, total_weight_label_s2, calories_per_g_label_s2, protein_label_s2, fat_label_s2, carb_label_s2, search_input_s2, food_menu_s2, ' ккал',))
add_button_s2.bind(on_press=lambda instance: addition(the_path + 'caloriecount_s2.txt', the_path + 'log_s2.txt', log_s2, selection_button_s2, portion_input_s2, ingredients_dict, calories_label_s2, total_weight_label_s2, calories_per_g_label_s2, protein_label_s2, fat_label_s2, carb_label_s2, search_input_s2, food_menu_s2, ' ккал',))

#RECIPESCREEN (Screen 3 - s3)
recipe_sorter_s3 = {}

RecipeScreen = Screen(name='Recipes')

#Elements s3
reset_s3 = Button(background_normal='Fenix.jpg', background_down='Fenix.jpg', size_hint=(0.65,1), pos_hint={'center_x': .5, 'center_y': .5})
selection_button_s3 = Button(text='Яств рецепты', background_color=(0,0,0,0), font_name=teremokfont, font_size=mainmenufontsize) #, size_hint=(0.5, 0.5)
recipe_menu_s3 = DropDown()
search_input_s3 = TextInput(text='', multiline=False, font_name=teremokfont, font_size=120, size_hint=(0.25, 0.5)) #background_color=(0,0,0,0), foreground_color=(1,1,1,1),
spacer1_s3 = Label(text='Filler', font_name=teremokfont, color=(0,0,0,0), pos_hint={'center_x': .5, 'center_y': .5})
recipe_label_s3 = Label(text='', font_name=teremokfont, font_size=90, color=(1,1,1,1), pos_hint={'center_x': .5, 'center_y': .5})
spacer2_s3 = Label(text='Filler', font_name=teremokfont, color=(0,0,0,0), pos_hint={'center_x': .5, 'center_y': .5})

recipescreenlayout = BoxLayout(orientation='vertical')
recipescreenlayout.add_widget(reset_s3)
recipescreenlayout.add_widget(selection_button_s3)
recipescreenlayout.add_widget(spacer1_s3)
recipescreenlayout.add_widget(recipe_label_s3)
recipescreenlayout.add_widget(spacer2_s3)

RecipeScreen.add_widget(recipescreenlayout)

#LOGIC
dropdownmenu(recipe_dict, recipe_menu_s3)
selection_button_s3.bind(on_release=lambda instance: dropsearch(recipe_menu_s3, selection_button_s3, search_input_s3, recipe_sorter_s3, recipe_dict))
recipe_menu_s3.bind(on_select=lambda instance, x: dropdownbind(x, selection_button_s3, selection_button_s3, recipe_label_s3))

#Screen Carousel
carousel = Carousel(direction='right')
carousel.add_widget(MainScreen)
carousel.add_widget(DietCounterScreen)
carousel.add_widget(FoodCounterScreen)
carousel.add_widget(RecipeScreen)

class MainApp(App):
    def build(self):
        return carousel
    
if __name__ == '__main__':
    MainApp().run()