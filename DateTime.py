#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 19:58:35 2023

@author: alexandralozser
"""

# ----------------------------
# DateTime in Python
# ----------------------------


import datetime

date1 = datetime.date(2014, 12, 31)

# read only - can't be reassigned

year = date1.year
month = date1.month
day = date1.day

# ' date1.year = 2019 ' returns error


year1 = 2018
month1 = 11
day1 = 30

date2 = datetime.date(year1, month1, day1)

# Creating time variable

time1 = datetime.time(23, 59, 59, 1000)
print(time1)

# Get the date as well as time

dt = datetime.datetime(2023, 2, 25)

# Today
d1 = datetime.datetime.today()



# -------------------------------------

# Date processing and manipulations
