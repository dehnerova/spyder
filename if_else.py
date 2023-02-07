#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 21:23:29 2023

@author: alexandralozser
"""

# accept the input from the user

salary = int(input("Please enter your salary: "))

# condition for salary -> if salary is greater than 5000
if salary > 5000:
    print("Congratulations, your loan is approved")
else:
    print("Sorry, your loan was rejected")
    
    
# use of boolean variable in if-else
var1 = True

if var1:
    print("Value is true")
else:
    print("value is false")


# checking if variable is empty

# if int is 0 and you're checking if it has a value, 0 is false (no value)
var_str = 0

if var_str:
    print("this variable is neither empty or zero")
else:
    print("variable is empty")

    
# passing in an if statement

# pass = dont do anything if there is value, else display error

var_str2 = 10

if var_str2:
    pass
else:
    print("variable is empty")

    



# short hand "if" statement overview

# no else to the statement 
#ex: if salary > 5000: print("Approved")

# with else statement (notice no colons)
#ex: print("Approved") if salary > 5000 else print("Not approved")