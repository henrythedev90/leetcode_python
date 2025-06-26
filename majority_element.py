from typing import List
# 169. Majority Element
# Easy
# Topics
# premium lock icon
# Companies
# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

def majority_element(nums: List[int]) -> int:
    nums_len = len(nums)
    dictionary = {}
    checker = nums_len/2
    for i in nums:
        if i not in dictionary:
            dictionary[i] = 1
        else:
            dictionary[i] = dictionary.get(i, 0) + 1
        
        if dictionary[i] > checker:
            return i
        
print(majority_element([3,2,3]))
print(majority_element([2,2,1,1,1,2,2]))