#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 21:57:44 2023

@author: alexandralozser
"""
# ===========================================
# strftime and strptime for date formatting
# 
# strftime - date    --> string format
# strptime - string  --> date format

# d - dd
# m - mm
# y - yy
# Y - yyyy

# H - hh
# M - mm
# S - ss
#
# a - Three letter weekday
# A - Full name of the weekday
# w - Day number starting from Monday
# 
# b - Three letter month
# B - Full name of the month
# m - month number
# ===========================================
from datetime import datetime

date1 = datetime(2017, 11, 10, 21, 45, 19)

str(date1) 

# dd-mm-yyyy format
datetime.strftime(date1, '%d-%m-%Y')

# HH:MM:SS
datetime.strftime(date1, '%H:%M:%S')

# Weekday 
d_a = datetime.strftime(date1, '%a')
d_A = datetime.strftime(date1, '%A')
d_w = datetime.strftime(date1, '%w')

# 12 Hour time
datetime.strftime(date1, '%I:%M:%S %p')

# strptime
date2_str = '19/06/2018'

date2_d   = datetime.strptime(date2_str, '%d/%m/%Y')


