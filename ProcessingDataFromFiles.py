#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 17:57:37 2023

@author: alexandralozser
"""

# Open the file
file1 = open('/Users/alexandraLozser/Desktop/Python Masterclass Materials/Skillshare Classroom Handsons/sales.txt', 'ra')

# Read all the records from the current pointer
#records = file1.readlines()

# READLINES IS NOT RECOMMENDED WHEN USING LARGE FILES


total_2 = 0.0

for record in file1:
    order_id, trans_value = record.split(",")
    total_2 += float(trans_value)
    
   
# specifying how many digits after the period do we want
total = round(total_2, 2)

