#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#format()

# The total order value for Mr. Gates is $2000

user_name = "Gates"

order_value = int(input("Please enter the order value : "))

# 1 way. format by sequence
result = "the total order value for Mr. {} is ${}."
result.format(user_name, order_value)


# 2nd way. format by numeric indexes
result = "Customer name is Mr. {0}. The total order value for Mr. {0} is ${1}."
result.format(user_name, order_value)

# 3rd way. format by named indexes or keys
result = "the total order value for Mr. {name} is ${value}."
result.format(name=user_name, value=order_value)