#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 20:22:27 2023

@author: alexandralozser
"""

# ----------------------------------------------------------------------------

# Common methods using Lists

# ----------------------------------------------------------------------------



# Accept the input list from user

varT = True
num_list = []


# Accept input until user enters 0
while varT:
    num = int(input("Enter a number: "))
    
    if num == 0:
        varT = False
    else:
        num_list.append(num)

# ----------------------------------------------------------------------------


# Finding the length of the list/ num of elements
len(num_list)

# ----------------------------------------------------------------------------

# Concatenate the lists

list2 = [45, 15, 35]

conList = num_list + list2


# ----------------------------------------------------------------------------


# num_list = num_list + list2  <- can add contents of list2 to num_list
# OR
# use extend() method

num_list.extend(list2)


# ----------------------------------------------------------------------------


# Calculating the average of the list

# using sum method to add all the variables, then dividing them by the num of elements
average = sum(num_list)/len(num_list)


# same thing below, except more steps
total = 0

for num in num_list:
    total += num
    
newAv = total/len(num_list)


# ----------------------------------------------------------------------------

# Sorting the contents of a list

num_list.sort(reverse=True)


# ----------------------------------------------------------------------------

# Using index method to find out at what position an element is


snum = int(input("please enter the number to search for: "))

position = num_list.index(snum)

print("we have found the number {} at position {}.".format(snum, position))


# 2 IMPORTANT TIPS about index()

# 1. Only returns the first index value 
# 2. Returns valueError if no match is found






