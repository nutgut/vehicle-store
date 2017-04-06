#!/usr/bin/python
# coding=utf-8
""""
This program is a simple vehicle store.
As normal user you can search for vehicles in the store.
As manager you can also buy and sell vehicles.
First version of this program will save vehicles in a list or dictionary.
My plan is to change the save settings to a text file at next version.
"""

import menu
import vehicle
# import users
import adminMenu
from sys import exit


def main():
    print '\nWelcome to Vehicle Shop System 0.1'
    this_menu = menu.MainMenu()  # Create object from the class MainMenu

    while True:
        this_menu.get_main_menu()  # Get the menu
        user_input = raw_input('> ')
        choice(user_input)


# User choice
def choice(arg):
    if arg == '1':
        list_vehicle(False)  # Tells if user is admin or not
    elif arg == '2':
        login()
    else:
        the_end()


def list_vehicle(args):
    printing = vehicle.Vehicle()
    print 'Type in a brand'
    brand = raw_input('> ')
    printing.get_vehicle(brand)
    print 'New search? (y) or (n)'
    user_input = raw_input('> ')
    if user_input == 'y':
        list_vehicle(args)
    elif user_input == 'n' and args is True:
        admin_menu()
    elif user_input == 'n' and args is False:
        # menu = Vehicle.MainMenu()
        # menu.get_main_menu()
        pass
    else:
        print 'Bye bye'
        exit(0)


def login():
    # logins = menu.MainMenu()
    admin_logins = adminMenu.Admin()
    print 'Enter your password'
    user_input = raw_input('> ')
    admin_logins.get_admin(user_input)
    if admin_logins.get_admin(user_input) == 'ok':
        admin_menu()
    else:
        print 'Wrong password'


def admin_menu():
    admin_logins = adminMenu.Admin()
    admin_logins.get_admin_menu()
    user_input = raw_input('> ')
    if user_input == '1':
        list_vehicle(True)
    elif user_input == '2':
        add_vehicles()
        # print vehicles
        pass
    else:
        the_end()


# Här ska jag fortsätta
def add_vehicles():
    vehicle_list = []
    print 'Enter five values'
    brand = raw_input('Enter brand: ')
    year = raw_input('Enter a year: ')
    model = raw_input('Enter a model: ')
    color = raw_input('Enter a color: ')
    price = raw_input('Enter a price: ')
    # print brand, year, model
    # info = ''.join([brand, year, model, color, price])
    # info = ' '.join(brand + year + model + color + price)
    info = [brand, year, model, color, price]
    # print ', '.join(info)
    new_vehicle = vehicle.Vehicle()
    # print new_vehicle
    new_vehicle.set_vehicle(brand, year, model, color, price)
    new_vehicle.get_vehicle(info)
    # new_vehicle = vehicle.Vehicle.set_vehicle(brand, year, model, color, price)
    # vehicle_list.append(new_vehicle)
    admin_menu()


def the_end():
    exit(0)


main()
