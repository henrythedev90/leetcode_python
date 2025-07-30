from typing import List
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2

def subarraySum(self, nums: List[int], k: int) -> int:
    total_sum = 0
    current_sum = 0
    prefix_count = {0:1}
    for num in nums:
        current_sum += num
        num_needed = current_sum - k
        if num_needed in prefix_count:
            total_sum += prefix_count.get(num_needed, 0)
        prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1
    return total_sum

# Test cases
def test_subarraySum():
    # Create an instance to call the method
    class Solution:
        def subarraySum(self, nums: List[int], k: int) -> int:
            return subarraySum(self, nums, k)
    
    solution = Solution()
    
    # Test case 1: Example from problem description
    nums1 = [1, 1, 1]
    k1 = 2
    result1 = solution.subarraySum(nums1, k1)
    expected1 = 2
    print(f"Test 1: nums={nums1}, k={k1}")
    print(f"Expected: {expected1}, Got: {result1}")
    print(f"Pass: {result1 == expected1}")
    print()
    
    # Test case 2: Example from problem description
    nums2 = [1, 2, 3]
    k2 = 3
    result2 = solution.subarraySum(nums2, k2)
    expected2 = 2
    print(f"Test 2: nums={nums2}, k={k2}")
    print(f"Expected: {expected2}, Got: {result2}")
    print(f"Pass: {result2 == expected2}")
    print()
    
    # Test case 3: Edge case - single element
    nums3 = [5]
    k3 = 5
    result3 = solution.subarraySum(nums3, k3)
    expected3 = 1
    print(f"Test 3: nums={nums3}, k={k3}")
    print(f"Expected: {expected3}, Got: {result3}")
    print(f"Pass: {result3 == expected3}")
    print()
    
    # Test case 4: Edge case - no solution
    nums4 = [1, 2, 3, 4]
    k4 = 10
    result4 = solution.subarraySum(nums4, k4)
    expected4 = 1  # [1, 2, 3, 4] sums to 10
    print(f"Test 4: nums={nums4}, k={k4}")
    print(f"Expected: {expected4}, Got: {result4}")
    print(f"Pass: {result4 == expected4}")
    print()
    
    # Test case 5: Edge case - negative numbers
    nums5 = [-1, -1, 1]
    k5 = 0
    result5 = solution.subarraySum(nums5, k5)
    expected5 = 1
    print(f"Test 5: nums={nums5}, k={k5}")
    print(f"Expected: {expected5}, Got: {result5}")
    print(f"Pass: {result5 == expected5}")
    print()
    
    # Test case 6: Edge case - multiple solutions
    nums6 = [1, -1, 1, -1, 1]
    k6 = 0
    result6 = solution.subarraySum(nums6, k6)
    expected6 = 6
    print(f"Test 6: nums={nums6}, k={k6}")
    print(f"Expected: {expected6}, Got: {result6}")
    print(f"Pass: {result6 == expected6}")
    print()
    
    # Test case 7: Edge case - target is 0
    nums7 = [0, 0, 0, 0, 0]
    k7 = 0
    result7 = solution.subarraySum(nums7, k7)
    expected7 = 15
    print(f"Test 7: nums={nums7}, k={k7}")
    print(f"Expected: {expected7}, Got: {result7}")
    print(f"Pass: {result7 == expected7}")
    print()
    
    # Test case 8: Edge case - large numbers
    nums8 = [1000, 2000, 3000, 4000]
    k8 = 6000
    result8 = solution.subarraySum(nums8, k8)
    expected8 = 1
    print(f"Test 8: nums={nums8}, k={k8}")
    print(f"Expected: {expected8}, Got: {result8}")
    print(f"Pass: {result8 == expected8}")
    print()
    
    # Test case 9: Edge case - all elements are the same
    nums9 = [2, 2, 2, 2, 2]
    k9 = 4
    result9 = solution.subarraySum(nums9, k9)
    expected9 = 4
    print(f"Test 9: nums={nums9}, k={k9}")
    print(f"Expected: {expected9}, Got: {result9}")
    print(f"Pass: {result9 == expected9}")
    print()
    
    # Test case 10: Edge case - empty array (should handle gracefully)
    nums10 = []
    k10 = 5
    result10 = solution.subarraySum(nums10, k10)
    expected10 = 0
    print(f"Test 10: nums={nums10}, k={k10}")
    print(f"Expected: {expected10}, Got: {result10}")
    print(f"Pass: {result10 == expected10}")
    print()

if __name__ == "__main__":
    test_subarraySum()