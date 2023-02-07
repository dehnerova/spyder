#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 21:41:37 2023

@author: alexandralozser
"""

salary = int(input("Please enter your salary: "))

age = int(input("Please enter your age: "))

# new line
print("")

if salary >= 7000 or age >= 45:
#if salary >= 7000 and age >= 45:
    print("auto approved")
else:
    print("approved manually")
    

# checking if a value is present in a statement using if and "in"

string = "python is programming is fun"

sub = input("Please enter the keyword to search: ")

print("")

if sub in string:
    print("keyword '"  + sub + "' is present")
else:
    print("search is empty")