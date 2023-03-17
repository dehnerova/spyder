#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 21:51:08 2023

@author: alexandralozser
"""

# --------------------------------------------
# Methods and functions of date
# --------------------------------------------
from datetime import date

date1 = date(2017, 10, 25)

# Replace method
# Necessary to make date1 = date1.replace*** because dates are immutable. 
# You have to reassign the value since you can't edit
date1 = date1.replace(year=2018)

# str for converting date to string
str(date1)

#ISO Format Date
date.isoformat(date1)

# String (ISO Format) to Date
date_str = str(date1)

date_iso = date.fromisoformat(date_str)

# Get weekday 
# 1 - Monday
# 2 - Tuesday
# 3 - Wednesday
# 4 - Thursday
# 5 - Friday
# 6 - Saturday
# 7 - Sunday
# 
date1.isoweekday()



