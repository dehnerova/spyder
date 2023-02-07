#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 21:36:36 2023

@author: alexandralozser
"""

#Create a program that asks the user to enter their name and their age.
#Print out a message addressed to them  
#that tells them the year that they will turn 100 years old.

name = input("your name please: ")
age = int(input("and your age is...? "))


def decadeOld(age):
    if age < 100:
        until100 = 100 - age
        return until100
    elif age > 100:
        return("NA")
    
result = ("Hello {name}, you'll turn 100 years old in {until100} years")
result.format(name=name, until100=decadeOld(age))




import datetime

name = input("What is your name: ")
age = int(input("How old are you: "))

#today = datetime.date.today().year <- alternative. maybe cleaner
year = str(datetime.date.today().year - age + 100)

print(name + ", you will be 100 years old in the year " + year)