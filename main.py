# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 23:40:42 2020

@author: vntom
"""

from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.carousel import Carousel
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen



DietCounterScreen = Screen(name='DietCounter')
FoodCounterScreen = Screen(name='FoodCounter')

dietcounterscreen_button = Button(text='MainScreen')

foodcounterscreen_button = Button(text='FoodCounter')

dietcounterscreenlayout = BoxLayout()
dietcounterscreenlayout.add_widget(dietcounterscreen_button)

foodcounterscreenlayout = BoxLayout()
foodcounterscreenlayout.add_widget(foodcounterscreen_button)

DietCounterScreen.add_widget(dietcounterscreenlayout)
FoodCounterScreen.add_widget(foodcounterscreenlayout)

carousel = Carousel(direction='right')
carousel.add_widget(DietCounterScreen)
carousel.add_widget(FoodCounterScreen)

keyboard = Window.request_keyboard(None, foodcounterscreen_button, 'text')
#foodcounterscreen_button.bind(on_release=keyboard)

class MyMainApp(App):
    def build(self):
        return carousel


if __name__ == "__main__":
    MyMainApp().run()