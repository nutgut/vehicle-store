#!/usr/bin/python
# coding=utf-8

from menu import MainMenu


# Class for administration menu
class Admin(MainMenu):
    def __init__(self):
        MainMenu.__init__(self)
        self._user = 'boss'
        self._menu_holder = ['\nMake a choice with numbers',
                             '\n1. Search for a vehicle',
                             '2. Add a vehicle',
                             '3. Delete a vehicle',
                             '4. Logout as administrator',
                             '5. Quit']

    def get_admin(self, password):
        if password == self._user:
            self._admin = True
            return 'ok'
        else:
            pass

    def get_admin_menu(self):
        for i in self._menu_holder:
            print (i)
