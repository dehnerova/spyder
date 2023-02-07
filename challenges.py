#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 17:38:03 2023

@author: alexandralozser
"""
# Calculate the multiplication and sum of two numbers
# Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.



def getProduct(num1, num2):
    
    result = num1 * num2
    
    if result <= 1000:
        print(result)
    else:
        print(num1+num2)
         
        



getProduct(20, 30)