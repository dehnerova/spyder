#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 19:52:06 2023

@author: alexandralozser
"""

def myFunction():
    print("this is my mothafucking first function in python")
    
    
myFunction()

def multiply(num1, num2):
    result = num1*num2
    return result

# define a function to do multiplication
num1 = int(input("please enter first num: "))
num2 = int(input("please enter second num: "))

result = multiply(num1, num2)

print("{} and {} multiplied is {}".format(num1, num2, result))