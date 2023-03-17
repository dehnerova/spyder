#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 20:00:55 2023

@author: alexandralozser
"""

income = int(input("please submit your annual income: "))
gender = input("please enter your gender: ")
tax = 0.0

def taxCalculator(income):
    if income > 100000:
        tax = float(income * .30)
    elif income >= 50000:
        tax = float(income * .20)
        tax = rebate(tax, gender)
    elif income < 50000:
        tax = float(income * 0.10)
        tax = rebate(tax, gender)
    else:
        return("Not valid income amount for tax calculator")       
    return tax


def rebate(tax, gender):
    if gender == "f":
        tax = tax - 500
        if tax < 0:
            tax = 0        
    return tax

tax = taxCalculator(income)
print("if your income is {}, then the tax collected is {}. You are left annually with {}".format(income, tax, income-tax))