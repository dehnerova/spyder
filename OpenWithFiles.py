#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 19:43:24 2023

@author: alexandralozser
"""

# FIRST WAY OF OPENING A FILE AND WRITING TO A NEW ONE
file1 = open('/Users/alexandraLozser/Desktop/Python Masterclass Materials/Skillshare Classroom Handsons/sales.txt', 'r')
file2 = open('newsales.txt', 'w')

for record in file1:
    file2.write(record)
    
    
    
#close the files
file1.close()
file2.close()


print(file1.closed)
print(file2.closed)

# ABOVE WAY OF OPENING, READING, AND WRITING TO A NEW FILE WORKS BUT YOU HAVE TO MAKE SURE TO CLOSE THE FILES BEFORE THE WRITING IS TRANSFERRED.


with open('sales.txt', 'r') as file1:
    with open('newsales.txt', 'w') as file2:
        for record in file1:
            file2.write(record)
            
# THIS WAY OF OPENING AND WRITING HAS ITS UPS AND DOWNS, BUT AT LEAST IT DOES NOT REQUIRE YOU TO CLOSE THE FILE MANUALLY