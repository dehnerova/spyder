#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 20:37:31 2023

@author: alexandralozser
"""

#C Code example

#int i;
#for (i=0; i<10; i=i+2):
#    {
#     printf("%d", i);
#     }


#Java Code example
#for (int i=0; i < 10; i++) {
# System.out.println(i);
#}


#Python Code example
#for variables in sequence:
    #statements
    

name = input("Please enter a name: ")

i = 1

for letters in name:
    print("character number {} is {} ".format(i, letters))
    i += 1
    
    
    
    
# --------------------------------------------------------------------------- 
# For loop using range
# --------------------------------------------------------------------------- 

for i in range(1, 10, 2):
    print(i)
    
nameRange = input("Please enter a name: ")

# i needs to start at 0, end at the end of the name

length = len(nameRange)


for j in range(0, length, 1):
    print("character number {} is {} ".format(j+1, nameRange[j])) #adding +1 to j so that the first character is 1 and not 0
    j += 1
    
    
# --------------------------------------------------------------------------- 
# For loop using enumerate
# --------------------------------------------------------------------------- 

# Accept input from the user

nameEnum = input("Please enter a name: ")

# Initializing x not necessary
# x = 1

# Run the for loop
# This allows you to increment x without needing to explicitly write x+=1
for x, letters in enumerate(nameEnum, start=1):
    print("character number {} is {} ".format(x, letters))
#    x += 1
    
