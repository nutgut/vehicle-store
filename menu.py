#!/usr/bin/python
# coding=utf-8


# Class for menu
class MainMenu(object):
    def __init__(self):
        self._admin = False
        self._menu_holder = ['\nMake a choice with numbers',
                             '\n1. Search for a vehicle',
                             '2. Login as administrator',
                             '3. Quit']

    def get_main_menu(self):
        for i in self._menu_holder:
            print (i)
