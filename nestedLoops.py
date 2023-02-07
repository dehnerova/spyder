#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 21:51:11 2023

@author: alexandralozser
"""

# ---------------------------------------------------------------------------
# Use of nested for loop for creating the table of numbers from 1-19
# ---------------------------------------------------------------------------

for i in range(1, 20, 1):
    print("")
    for j in range(1, 11, 1):
        result = i * j
        print(result, end=" ")
        
        
# ---------------------------------------------------------------------------        
# Printing a table for even numbers only
# ---------------------------------------------------------------------------

for i in range(1, 20, 1):
    if (i%2) != 0:
        continue
    
    for j in range(1, 11, 1):
        result = i * j
        print(result, end=" ")
        
    print("")
    
    
# ---------------------------------------------------------------------------
# Printing a table only up to 10.
# ---------------------------------------------------------------------------

for i in range(1, 20, 1):
    
    if i > 10:
        break
    
    for j in range(1, 11, 1):
        result = i * j
        print(result, end=" ")
        
    print("")
