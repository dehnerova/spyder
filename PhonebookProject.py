#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 22:50:20 2023

@author: alexandralozser
"""
# ~ Phonebook Project ~
# ----------------------------------------------------------------------------


# boolean for if the user has selected to stay in the menu
isStaying = True

# list for storing dictionary entries
list = []

phonebook = []
# dictionary for storing contact info
#phonebook = {"Name":[],"Number":[],"Email":[]};


print("Hello! Welcome to your personal Contact book.")



selectionLower = "enter"


while isStaying and selectionLower != "e":
    
    selection = input("\nWould you like to -\n\n1. S = Search for a contact.\n2. A = Add a new contact.\n3. E = Exit the system.\n")
    selectionLower = selection.lower()
    
    
    if selectionLower == "s" or selectionLower == "search":
        print("searching")
        
        searchName = input("Enter name to search: ")
        
        for list in phonebook:
            if searchName in list:
                print("We have found the name")
            else:
                print("we have not found the name YET")
     
        
    elif selectionLower == "a" or selectionLower =="add":
        
        name = input("First and Last name: ")
        number = int(input("Contact number: "))
        email = input("Enter email address: ")
        
        list = [name, number, email]
     
        print(list)
        
        phonebook.append(list)
        
    elif selectionLower == "e" or selectionLower == "exit":
        isStaying = False
        print("Exiting. Goodbye.")
    else:
        print("Not a valid option. Please choose S, A, or E to exit.")
