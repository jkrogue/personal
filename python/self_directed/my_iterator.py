# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
class RandomIterable:
    def __iter__(self):
        return self
    def __next__(self):
        if random.choice(["go", "go", "stop"]) == "stop":
            raise StopIteration  # signals "the end"
        return 1

class RevList:
    def __init__(self, limit):
        self.list = list(range(limit,0,-1))
    
    def __iter__(self):
        self.count = 0 # primed and ready to iterate
        return self
    
    def __getitem__(self, index):
        return self.list[index]
    
    def __next__(self):
        if self.count == len(self.list):
            raise StopIteration
        item = self.list[self.count]
        self.count += 1
        return item
        
        
my_iter = RevList(10)

print(my_iter[3])
for eggs in my_iter:
    print (eggs)
    
for eggs in RandomIterable():
    print(eggs)
