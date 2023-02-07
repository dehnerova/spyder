#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 22:49:08 2023

@author: alexandralozser
"""

# accept the salary from the user
salary = int(input("Please enter your salary: "))

# if-else conditions
if salary >= 7000:
    print("Automatically approved loan")
else:
    if salary >= 5000:
        print("manually approved")
    else:
        print("rejected")
        
        
# elif

salary = int(input("Please enter your salary: "))

if salary >= 7000:
    print("Automatically approved loan")
elif salary >= 5000:
        print("manually approved")
else:
        print("rejected")