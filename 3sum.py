from typing import List
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.

def threeSum(self, nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        a = nums[i]
        left = i + 1
        right = len(nums) - 1
        while left < right:
            total = a + nums[left] + nums[right]
            if total == 0:
                result.append([a, nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return result

# Test cases
def test_threeSum():
    # Create an instance to call the method
    class Solution:
        def threeSum(self, nums: List[int]) -> List[List[int]]:
            return threeSum(self, nums)
    
    solution = Solution()
    
    # Test case 1: Example from problem description
    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = solution.threeSum(nums1)
    expected1 = [[-1, -1, 2], [-1, 0, 1]]
    print(f"Test 1: nums={nums1}")
    print(f"Expected: {expected1}")
    print(f"Got: {result1}")
    print(f"Pass: {sorted([sorted(triplet) for triplet in result1]) == sorted([sorted(triplet) for triplet in expected1])}")
    print()
    
    # Test case 2: Example from problem description
    nums2 = [0, 1, 1]
    result2 = solution.threeSum(nums2)
    expected2 = []
    print(f"Test 2: nums={nums2}")
    print(f"Expected: {expected2}")
    print(f"Got: {result2}")
    print(f"Pass: {result2 == expected2}")
    print()
    
    # Test case 3: Example from problem description
    nums3 = [0, 0, 0]
    result3 = solution.threeSum(nums3)
    expected3 = [[0, 0, 0]]
    print(f"Test 3: nums={nums3}")
    print(f"Expected: {expected3}")
    print(f"Got: {result3}")
    print(f"Pass: {result3 == expected3}")
    print()
    
    # Test case 4: Edge case - all negative numbers
    nums4 = [-3, -2, -1, 0, 1, 2, 3]
    result4 = solution.threeSum(nums4)
    expected4 = [[-3, 0, 3], [-3, 1, 2], [-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]
    print(f"Test 4: nums={nums4}")
    print(f"Expected: {expected4}")
    print(f"Got: {result4}")
    print(f"Pass: {sorted([sorted(triplet) for triplet in result4]) == sorted([sorted(triplet) for triplet in expected4])}")
    print()
    
    # Test case 5: Edge case - no solution
    nums5 = [1, 2, 3, 4, 5]
    result5 = solution.threeSum(nums5)
    expected5 = []
    print(f"Test 5: nums={nums5}")
    print(f"Expected: {expected5}")
    print(f"Got: {result5}")
    print(f"Pass: {result5 == expected5}")
    print()
    
    # Test case 6: Edge case - many duplicates
    nums6 = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    result6 = solution.threeSum(nums6)
    expected6 = [[-1, 0, 1], [0, 0, 0]]
    print(f"Test 6: nums={nums6}")
    print(f"Expected: {expected6}")
    print(f"Got: {result6}")
    print(f"Pass: {sorted([sorted(triplet) for triplet in result6]) == sorted([sorted(triplet) for triplet in expected6])}")
    print()
    
    # Test case 7: Edge case - large numbers
    nums7 = [-1000, -500, 0, 500, 1000]
    result7 = solution.threeSum(nums7)
    expected7 = [[-1000, 0, 1000], [-500, 0, 500]]
    print(f"Test 7: nums={nums7}")
    print(f"Expected: {expected7}")
    print(f"Got: {result7}")
    print(f"Pass: {sorted([sorted(triplet) for triplet in result7]) == sorted([sorted(triplet) for triplet in expected7])}")
    print()
    
    # Test case 8: Edge case - minimum length array
    nums8 = [0, 0, 0, 0]
    result8 = solution.threeSum(nums8)
    expected8 = [[0, 0, 0]]
    print(f"Test 8: nums={nums8}")
    print(f"Expected: {expected8}")
    print(f"Got: {result8}")
    print(f"Pass: {result8 == expected8}")
    print()

if __name__ == "__main__":
    test_threeSum()
