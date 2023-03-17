#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 18:07:09 2023

@author: alexandralozser
"""

file1 = open('/Users/alexandraLozser/Desktop/Python Masterclass Materials/Skillshare Classroom Handsons/sales.txt', 'r')
file2 = open('salestype.txt', 'w')

# going through the file, checking if the second float is above 150.0
# if yes, add an H after
#if no, add an L after

comparator = 150.00

for record in file1:
    order_id, trans_value = record.split(",")
    
    if float(trans_value) < comparator:
        trans_type = "L"
    else:
        trans_type = "H"
            
    record = record.strip("\n")
    write_rec = record + "," + trans_type + "\n"
    file2.write(write_rec)
    
    
file1.close()
file2.close()