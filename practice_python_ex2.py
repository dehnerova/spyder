#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 22:35:13 2023

@author: alexandralozser
"""

#Ask the user for a number. 
#Depending on whether the number is even or odd, print out an appropriate message to the user. 
#Hint: how does an even / odd number react differently when divided by 2?

#If the number is a multiple of 4, print out a different message.

num = int(input("Please enter number: "))

def numCheck(num):
    if num % 4 == 0:
        return "divisible by 4"
    elif num % 2 == 0:
        return "num is even"
    else:
        return "num is odd"
    
print(numCheck(num))