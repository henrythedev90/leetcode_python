from typing import List
# 18. 4Sum
# Medium
# Topics
# premium lock icon
# Companies
# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.



# Example 1:

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# Example 2:

# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]

def four_sum(nums: List[int], target: int) -> List[int]:
    nums_length = len(nums)
    result = []

    if nums_length < 4:
        return result
    
    nums.sort()

    for i in range(nums_length - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, nums_length - 2):
            if j > i + 1 and nums[j] == nums[j - 2]:
                continue
            left = j + 1
            right = nums_length - 1

            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
    return result
    # Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
print(four_sum([1,0,-1,0,-2,2], target = 0))
# Example 2:
print(four_sum([2,2,2,2,2], 8))
# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]