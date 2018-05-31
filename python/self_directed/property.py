# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Car:
    
    POSSIBLE_MAKES = ("Toyota", "Ford", "General Motors", "Honda", "Hyundai")
    
    def __init__(self, make):
        self.make = make
        
        
    @property
    def make(self):
        print("Getter called")
        return self.__make
    
    @make.setter
    def make(self, make_name):
        if make_name in Car.POSSIBLE_MAKES:
            print("Setting to " + make_name)
            self.__make = make_name
        else:
            print(make_name + " not one of possible makes")
            

my_car = Car("Toyota")

print(my_car.make)

my_car.make = "Ford"

print(my_car.make)


my_car.make = "Lexus"
        
my_car._Car__make = "Lexus"
print(my_car.make)
