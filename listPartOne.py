#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 22:26:02 2023

@author: alexandralozser
"""

# ----------------------------------------------------------------------------
# Initialize and create a list variable using

# 1. Using initial set of values
# 2. Using empty square brackets
# 3. list() function
# 4. By assigning or copying the existing list.
# ----------------------------------------------------------------------------

# 1. 
list1 = ["Jitesh", "John", "Alex"]
print(list1)

# 2. 
# no values yet
list2 = []
print(list2)

# below is the same thing as above except using the list() function

#3. 
#list2 = list()
#print(list2)

# 4. 
# assigning the label, but everything remains in storage where it was
# referring to the same memory location, so changes are reflected in both places
list2 = list1

# values get moved to list3's new storage space
# copied and stored in a different location
list3 = list1.copy()

list1.append("Alia")


# ----------------------------------------------------------------------------
# Accessing list elements
# ----------------------------------------------------------------------------

print(list1[2])

#last element of the list
print(list1[-1])


# accessing a portion or range of the list

# if we wanted to get the list from the second variable to the last (which is 3),
# we mark it as starting from 1 (0 is the first), and end at 4 
# (3+1 to make sure the last element is included)

print(list1[1:4])


# printing from beginning to 2nd element (excluding the last)
print(list1[:3])


# printing from second element on (excluding first)
print(list1[1:])


# printing from start to finish
print(list1[:])


# Negative index range

# "-3" means 3 up from the last element
# "-2" means 2 up from the last element
print(list1[-3:-1])



# Accessing all the elements and process the data
for name in list1:
    print(name)



# Searching for an element in the list
searchName = input("Please enter the name to search: ")

if searchName in list1:
    print("We have found the name")
else:
    print("we have not found the name YET")
        






