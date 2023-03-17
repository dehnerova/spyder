#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 22:14:04 2023

@author: alexandralozser
"""

# ---------------------------------------------------
# File handling in Python
# Open, Read, Write and Close the file 
# ---------------------------------------------------


# 'r' : open for reading (default)

# 'w' : open for writing, truncating the file first

# 'x' : create a new file and open it for writing

# 'a' : open for writing, appending to the end of the file if it exists

# 'b' : binary mode

# 't' : text mode (default)

# '+' : open a disk file for updating (reading and writing)

# --------------------------------------------------------------------



# Open the file
file1 = open('/Users/alexandraLozser/Desktop/Python Masterclass Materials/Skillshare Classroom Handsons/sales.txt', 'ra')

# Check the open mode
file1.mode


# Read the file - One record at a time using readline 
record1 = file1.readline()

# Reposition the file pointer to the start (0)
file1.seek(0)

# Read all the records from the current pointer
records = file1.readlines()


# Close the file
file1.close()
