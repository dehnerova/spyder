#!/usr/bin/env python3
# -*- coding: utf-8 -*-
var_str = "My name is Alex"

print(var_str)


# assign multiple strings to a variable
#using 3 quotes
var_str2 = """My name is Alex.

I am learning Python"""

print(var_str2)

# using new line character
var_str3 = """My name is Alex.\nI am learning Python"""
print(var_str3)

# String as an array of characters / collection of character
# string indexing and slicing

var_str4 = "My name is Jitesh"

# accessing characters using index position (starts at 0)
print(var_str4[0])

#accessing a range of charcters, also known as slicing of the string
print(var_str4[3:7])

# accessing using negative index (starting from the end of the string)

print(var_str4[-6:-2])

#basic String operators
#concatenation of strings
var1 = "Hello"
var2 = "World"

var3 = var1 + " " + var2

#search for a substring using "in" and "not in"

"Hello" not in var3

# formatting operator of the string using %
print("My name is %s and my age is %i" %(("Alex", 24)))

# Raw string operator using r
# letter r before the quotes lets it know to read the string without special characters
varOne = r'C:\user\test.data'

print(varOne)

# Some basic functions and methods applied on String data types

var11 = "Programming is easy with Python"

# getting the length of the string
len(var11)

#count the number of characters in a string or substring
var11.count("i")

# find and index

var11.find("Python")
var11.index("Python")


#change case of the string
var11.upper()
var11.lower()

var12 = "Python"
print(var12)

var12.ljust(12)
var12.rjust(12)

var12.ljust(12, "-")






