#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 21:00:51 2023

@author: alexandralozser
"""

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

#----------------------------------------------------------------------------------------------------------------------------



#first way is to iterate through 2 loops at the same time and find if the combinations of the two indexes add up to the target number

class Solution:
    from typing import List
    
# self is optional, nums [] list of ints, and target written to the List[] of ints
    def twoSum(nums: List[int], target: int) -> List[int]:
    
        # d will be the dictionary in which we store 
        d = {}
    
        for i, j in enumerate(nums):
            r = target - j
            if r in d:
                return [d[r], i]
            d[j] = i
            
       
    listy = [2,4,2,1]
    twoSum(listy, 6)