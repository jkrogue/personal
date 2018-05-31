#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 18:15:43 2018

@author: jkrogue
"""
import pandas as pd

# define a class that I will use to record each response
class Response:
    def __init__(self, name):
        self.name = name
        self.count = 0
        
    def __str__(self):
        return self.name
        
def display_responses(list_responses):
    for i, each in enumerate(list_responses):
        print("%s\t%s %s" % (i, each, each.count))
     

str_responses = ["Retired","Young kids\\first baby","Not Married","Marriage problems", "Mental health challenges", "Health crisis", "Recent death", "LGBTQ", "Homeless", "Teenager", "Nonmember or inactive family member", "Struggling testimony", "Financial challenges", "Addiction", "Nothing in common"]
responses = []
for each in str_responses:
    responses.append(Response(each))

print("At any time press ctrl-c to quit")

def read_responses():
    filename = input("\n\nEnter filename to load responses: ")
    input_df = pd.read_csv(filename, index_col = 0)
    global responses
    responses = []
    for i, each in enumerate(input_df["number_responses"]):
        this_response = Response(input_df.index[i])
        this_response.count = int(each)
        responses.append(this_response)
    
def save_responses():
    filename = input("\n\nEnter filename to save responses: ")
    str_responses = []
    counts = []
    for each in responses:
        str_responses.append(each.name)
        counts.append(each.count)
    response_df = pd.DataFrame(index=str_responses,data=counts, columns=["number_responses"])
    sort_yn = input("Do you want to sort (y/n)? ")
    if sort_yn == "y":
        response_df = response_df.sort_values("number_responses",ascending = False)
    response_df.to_csv(filename)
    exit()

while True:
    try:
        display_responses(responses)
        str_idx = input("Enter index ('s' to save, 'o' to load, 'x' to exit): ")
        if str_idx is "":
            print("No index entered\n\n")
            continue
        elif str_idx == "s":
            save_responses()
        elif str_idx == "o":
            read_responses()
        elif str_idx == "x":
            save_yn = input("\n\nDo you want to save (y/n)? ")
            if save_yn == "y":
                save_responses()
            else:
                exit()
        else:
            idx_to_add = int(str_idx)
            if idx_to_add < 0 or idx_to_add >= len(responses):
                print("Index out of range\n\n")
                continue
            responses[idx_to_add].count += 1
            print("Incremented count of %s\n\n" % (responses[idx_to_add]))
    except KeyboardInterrupt as ki:
        save_responses()

