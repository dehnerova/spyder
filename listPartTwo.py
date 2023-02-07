#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 19:40:52 2023

@author: alexandralozser
"""

# ----------------------------------------------------------------------------
# Adding, updating, deleting elements of a list
# ----------------------------------------------------------------------------

# list1.append("Alia") <- can use this to add a variable, but it will always go to the end of the list

list1 = ["Jitesh", "John", "Alex"]
print(list1)

list2 = []
print(list2)

list2 = list1
list3 = list1.copy()


list1.append("Alia")

# Insert Method

# first parameter is the position
# second parameter is the element you're inserting
list1.insert(1, "Frans")


# Updating the element of replacing John with Chris
list1[2] = "Chris"


# Deleting an element

del list3[1]

# Same can be achieved using method "remove"

list3.remove("Jitesh")

# same result, to delete something
list3.pop(0)

# Clear all the elements of the list

list3.clear()