#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 14:45:11 2018

@author: jkrogue
"""

# my version of mpg_write program

import csv

class Trips:
    
    def __init__(self):
        self.trip_list = []
        
    def __iter__(self):
        self.count = 0
        return self
    
    def __next__(self):
        if len(self.trip_list) == self.count:
            raise StopIteration
        trip = self.trip_list[self.count]
        self.count += 1
        return trip
    
    def __getitem__(self,key):
        return self.trip_list[key]
    
    def __setitem__(self,key,value):
        self.trip_list[key] = value
    
    def load(self, filename):

        with open(filename,"r") as file:
            data_set = list(csv.reader(file))
            for each in data_set:
                self.trip_list.append(Trip(each[0],each[1],each[2]))
    
    def save(self, filename):
        with open (filename,"w",newline="") as file:
            data_set = []
            for each in self.trip_list:
                data_set.append(each.to_list())
            csv.writer(filename).writelines(data_set)

    def append(self, trip):
        try:
            self.trip_list.append(Trip(trip))
        except ValueError as error:
            print("Can't append a non-trip item to Trips object")
            
    def __str__(self):
        to_return = "Distance\tGallons\tMPG"
        for each in self.trip_list:
            to_return += "\n" + str(each)
        return to_return
        

class Trip:
    def __init__(self, distance, gallons, mpg):
        self.distance = float(distance)
        self.gallons = float(gallons)
        self.mpg = float(mpg)
        
    def to_list(self):
        return [self.distance,self.gallons,self.mpg]
        
    def __str__(self):
        return ("%i\t%.2f\t%.2f" % (self.distance, self.gallons, self.mpg))
       


def get_mpg():
    try:
        miles = float(input("\nEnter miles driven:\t"))
        gallons = float(input("Enter gallons of gas:\t"))
        mpg = miles/gallons
        print("Miles per gallon:\t%.2f\n" % (mpg))
        return Trip(miles,gallons,mpg)
    except ValueError as error:
        print("Didn't enter a number!\n")
    
def display_list(trip_list):
    print("Using my iterator:\nDistance\tGallons\tMPG")
    for each in trip_list:
        print(str(each))
    print("Using my __getitem__")
    for i, each in enumerate(trip_list):
        print(trip_listtest[i])

def main():
    trips = Trips()
    print("The Miles Per Gallon Application")
    trips.load(input("Enter filename to load: "))
    print("\n%s" % trips)
    while True:
        this_trip = get_mpg()
        if this_trip is not None:
            trips.append(this_trip)
        y_n = input("More entries? (y or n): ")
        if not(y_n.lower() == "y"):
            trips.save(input("Enter filename to save: "))
            exit("\nThanks for playing!\n")
            
if __name__ == "__main__":
    main()