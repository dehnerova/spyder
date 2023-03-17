#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 21:46:45 2023

@author: alexandralozser
"""

# Given 2 strings s1 and s2, check if they're anagrams.
# two strings are anagrams if they are made of the same characters with the same frequencies

# input: 
# s1 = danger
# s2 = garden
# returns true

s1 = input("Please enter first string: ")
s2 = input("Enter second string: ")

isAnagram = False


# first check if the length is the same for both

def isAnagram(s1, s2):
    if len(s1) != len(s2):
        return False
    else:
        print("same length")
        
        stringDictionary1 = {}
        stringDictionary2 = {}
        
        for ch in s1:
            if ch in stringDictionary1:
                stringDictionary1[ch] += 1
            else:
                stringDictionary1[ch] = 1
                
                
        for ch in s2:
            if ch in stringDictionary2:
                stringDictionary2[ch] += 1
            else:
                stringDictionary2[ch] = 1
                     
if isAnagram:
    print("{} and {} are anagrams".format(s1, s2))
else:
    print("Not anagrams")
    
    