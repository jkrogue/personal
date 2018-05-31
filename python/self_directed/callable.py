#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  6 20:27:14 2018

@author: jkrogue
"""

class MyCallableClass:
    
    def __init__(self, name):
        self.name = name
        
    # When an instance of MyCallableClass is called with two list parameter returns tuple of two lists with each value divided by 10
    # (simulates what is done when you call instance of basemap with lists of longtitude and latitude)
    def __call__(self, x, y):
        if type(x) != list or type(y) != list:
            raise ValueError("Instance of MyCallableClass must be called with two list parameters")
        conv_x = []
        conv_y = []
        for each in x:
            conv_x.append(each/10)
        for each in y:
            conv_y.append(each/10)
        return conv_x,conv_y

list_x = [10,100,1000]
list_y = [50,200]
print("Before conversion-\nx: %s\ny: %s\n\n" % (list_x,list_y))
mine = MyCallableClass("Justin")
list_x, list_y = mine(list_x,list_y)

print ("After division by 10-\nx: %s\ny: %s" % (list_x,list_y))