#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 21:41:41 2023

@author: alexandralozser
"""

from datetime import date, time, datetime, timedelta

# Subtraction of dates
date1 = datetime(2017, 11, 20, 1) #timedelta = difference of 10 days, 3000 seconds = 1 hour
date2 = datetime(2017, 11, 10)

date1 - date2 

# Duration in date terms, difference, interval

# setting one_day to 1 day using timedelta
one_day  = timedelta(days=1)
date1 = date1 + one_day

one_month = timedelta(days=30)

# Check if the date is within one month of today
# For statements, reminders, monthly statements

t_date = datetime(2020, 6, 21)

today = datetime.today()

# checking if today is within the 30 days or not

if (today - t_date) <= one_month:
    print("True")

else:
    print("False")


# timedelta syntax:
    
# timedelta(days=0, 
#           seconds=0, 
#           microseconds=0, 
#           milliseconds=0, 
#           minutes=0, 
#           hours=0, 
#           weeks=0)

# Multiplication of timedelta
one_month * 10

# Division
one_month /10

one_month / 12

30/12

12*60*60
