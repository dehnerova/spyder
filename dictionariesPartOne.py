#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 22:32:18 2023

@author: alexandralozser
"""

# ----------------------------------------------------------------------------

# Dictonaries


# Collection of key-value pairs

# Address = {'Street': '180 Adams Street', 'City': 'Chicago', 'State': "IL"}
# Address['Street'] -> '180 Adams Street'

# Can be used to convert to or from JSon format 

# ----------------------------------------------------------------------------


# Define and initialize dictionary

address = {'Street' : '180 Adams Street',
           'City'   :  'Chicago',
           'State'  : 'IL',
           'Country': 'USA'}


print(address['Country'])


# Add and Update value for particular key

# Updating 180 Adams to 181 Adams
address['Street'] = '181 Adams Street'


# Adding a new key to an existing dictionary
# Adding a zip code

address['Zip'] = '60611'


# Deleting a key value pair
del address['Zip']


# ----------------------------------------------------------------------------

# Functions and Methods using Dictonary

# Length of the dict
# This is provide num of keys
len(address)



# Method of Keys

# converting type dict_keys to list
keys = list(address.keys())


# values of the dictionary
# all the values extracted in a list
values = list(address.values())





