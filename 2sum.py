from typing import List
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

def twoSum(nums: List[int], target:int) -> List[int]:
    dict = {}
    for i, num in enumerate(nums):
        difference = target - num
        if difference in dict:
            return [dict[difference], i]
        dict[num] = i

# Test cases
def test_twoSum():
    # Test case 1: Example from problem description
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = twoSum(nums1, target1)
    expected1 = [0, 1]
    print(f"Test 1: nums={nums1}, target={target1}")
    print(f"Expected: {expected1}, Got: {result1}")
    print(f"Pass: {sorted(result1) == sorted(expected1)}")
    print()
    
    # Test case 2: Example from problem description
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = twoSum(nums2, target2)
    expected2 = [1, 2]
    print(f"Test 2: nums={nums2}, target={target2}")
    print(f"Expected: {expected2}, Got: {result2}")
    print(f"Pass: {sorted(result2) == sorted(expected2)}")
    print()
    
    # Test case 3: Example from problem description
    nums3 = [3, 3]
    target3 = 6
    result3 = twoSum(nums3, target3)
    expected3 = [0, 1]
    print(f"Test 3: nums={nums3}, target={target3}")
    print(f"Expected: {expected3}, Got: {result3}")
    print(f"Pass: {sorted(result3) == sorted(expected3)}")
    print()
    
    # Test case 4: Edge case - negative numbers
    nums4 = [-1, -2, -3, -4, -5]
    target4 = -8
    result4 = twoSum(nums4, target4)
    expected4 = [2, 4]  # -3 + -5 = -8
    print(f"Test 4: nums={nums4}, target={target4}")
    print(f"Expected: {expected4}, Got: {result4}")
    print(f"Pass: {sorted(result4) == sorted(expected4)}")
    print()
    
    # Test case 5: Edge case - zero in array
    nums5 = [0, 4, 3, 0]
    target5 = 0
    result5 = twoSum(nums5, target5)
    expected5 = [0, 3]  # 0 + 0 = 0
    print(f"Test 5: nums={nums5}, target={target5}")
    print(f"Expected: {expected5}, Got: {result5}")
    print(f"Pass: {sorted(result5) == sorted(expected5)}")
    print()
    
    # Test case 6: Edge case - large numbers
    nums6 = [1000000, 2000000, 3000000, 4000000]
    target6 = 5000000
    result6 = twoSum(nums6, target6)
    expected6 = [1, 2]  # 2000000 + 3000000 = 5000000
    print(f"Test 6: nums={nums6}, target={target6}")
    print(f"Expected: {expected6}, Got: {result6}")
    print(f"Pass: {sorted(result6) == sorted(expected6)}")
    print()
    
    # Test case 7: Edge case - solution at beginning and end
    nums7 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target7 = 11
    result7 = twoSum(nums7, target7)
    expected7 = [4, 5]  # 5 + 6 = 11
    print(f"Test 7: nums={nums7}, target={target7}")
    print(f"Expected: {expected7}, Got: {result7}")
    print(f"Pass: {sorted(result7) == sorted(expected7)}")
    print()
    
    # Test case 8: Edge case - duplicate numbers (not the solution)
    nums8 = [1, 1, 2, 3, 4, 5]
    target8 = 9
    result8 = twoSum(nums8, target8)
    expected8 = [4, 5]  # 4 + 5 = 9
    print(f"Test 8: nums={nums8}, target={target8}")
    print(f"Expected: {expected8}, Got: {result8}")
    print(f"Pass: {sorted(result8) == sorted(expected8)}")
    print()

if __name__ == "__main__":
    test_twoSum()
