#!/usr/bin/python
# coding=utf-8

# Class for vehicle store

# Not working yet!!!


class Vehicle(object):
    # Method for the main menu
    def __init__(self, brand='', year='', model='', color='', price=''):
        self._brand = brand
        self._year = year
        self._model = model
        self._color = color
        self._price = price
        self._admin = False   # Needed?

    def get_vehicle(self, arg):
        # if brand in self.__vehicles:
            # print (self.__vehicles[brand])
        print ', '.join(arg)

    def set_vehicle(self, brand, year, model, color, price):
        self._brand = brand
        self._year = year
        self._model = model
        self._color = color
        self._price = price

