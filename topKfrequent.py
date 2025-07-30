import operator
from typing import List

# Given an integer array nums and an integer k, return the k most frequent elements. 
# You may return the answer in any order.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]

def topKFrequent(nums: List[int], k: int) -> List[int]:
    dictionary = {}
    for num in nums:
        if num not in dictionary:
            dictionary[num] = 1
        else:
            dictionary[num] += 1
    
    # Sort by frequency (descending) and return top k elements
    sorted_items = sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True)
    result = [item[0] for item in sorted_items[:k]]
    return result

# Test cases
def test_topKFrequent():
    # Test case 1: Example from problem description
    nums1 = [1, 1, 1, 2, 2, 3]
    k1 = 2
    result1 = topKFrequent(nums1, k1)
    expected1 = [1, 2]
    print(f"Test 1: nums={nums1}, k={k1}")
    print(f"Expected: {expected1}, Got: {result1}")
    print(f"Pass: {sorted(result1) == sorted(expected1)}")
    print()
    
    # Test case 2: Example from problem description
    nums2 = [1]
    k2 = 1
    result2 = topKFrequent(nums2, k2)
    expected2 = [1]
    print(f"Test 2: nums={nums2}, k={k2}")
    print(f"Expected: {expected2}, Got: {result2}")
    print(f"Pass: {result2 == expected2}")
    print()
    
    # Test case 3: Edge case - all elements have same frequency
    nums3 = [1, 2, 3, 4, 5]
    k3 = 3
    result3 = topKFrequent(nums3, k3)
    expected3 = [1, 2, 3]  # Any 3 elements since all have frequency 1
    print(f"Test 3: nums={nums3}, k={k3}")
    print(f"Expected: {expected3}, Got: {result3}")
    print(f"Pass: {len(result3) == k3 and all(x in nums3 for x in result3)}")
    print()
    
    # Test case 4: Edge case - k equals array length
    nums4 = [1, 1, 2, 2, 3]
    k4 = 3
    result4 = topKFrequent(nums4, k4)
    expected4 = [1, 2, 3]
    print(f"Test 4: nums={nums4}, k={k4}")
    print(f"Expected: {expected4}, Got: {result4}")
    print(f"Pass: {sorted(result4) == sorted(expected4)}")
    print()
    
    # Test case 5: Edge case - negative numbers
    nums5 = [-1, -1, -1, 2, 2, 3, 3, 3, 3]
    k5 = 2
    result5 = topKFrequent(nums5, k5)
    expected5 = [3, -1]  # 3 appears 4 times, -1 appears 3 times
    print(f"Test 5: nums={nums5}, k={k5}")
    print(f"Expected: {expected5}, Got: {result5}")
    print(f"Pass: {sorted(result5) == sorted(expected5)}")
    print()
    
    # Test case 6: Edge case - large numbers
    nums6 = [1000, 1000, 2000, 2000, 2000, 3000]
    k6 = 2
    result6 = topKFrequent(nums6, k6)
    expected6 = [2000, 1000]  # 2000 appears 3 times, 1000 appears 2 times
    print(f"Test 6: nums={nums6}, k={k6}")
    print(f"Expected: {expected6}, Got: {result6}")
    print(f"Pass: {sorted(result6) == sorted(expected6)}")
    print()
    
    # Test case 7: Edge case - k = 1
    nums7 = [1, 1, 1, 2, 2, 3, 4, 5, 6]
    k7 = 1
    result7 = topKFrequent(nums7, k7)
    expected7 = [1]  # 1 appears most frequently (3 times)
    print(f"Test 7: nums={nums7}, k={k7}")
    print(f"Expected: {expected7}, Got: {result7}")
    print(f"Pass: {result7 == expected7}")
    print()
    
    # Test case 8: Edge case - empty array
    nums8 = []
    k8 = 0
    result8 = topKFrequent(nums8, k8)
    expected8 = []
    print(f"Test 8: nums={nums8}, k={k8}")
    print(f"Expected: {expected8}, Got: {result8}")
    print(f"Pass: {result8 == expected8}")
    print()
    
    # Test case 9: Edge case - all same elements
    nums9 = [5, 5, 5, 5, 5]
    k9 = 1
    result9 = topKFrequent(nums9, k9)
    expected9 = [5]
    print(f"Test 9: nums={nums9}, k={k9}")
    print(f"Expected: {expected9}, Got: {result9}")
    print(f"Pass: {result9 == expected9}")
    print()
    
    # Test case 10: Edge case - k larger than unique elements
    nums10 = [1, 2, 3]
    k10 = 5
    result10 = topKFrequent(nums10, k10)
    expected10 = [1, 2, 3]  # Should return all unique elements
    print(f"Test 10: nums={nums10}, k={k10}")
    print(f"Expected: {expected10}, Got: {result10}")
    print(f"Pass: {sorted(result10) == sorted(expected10)}")
    print()

if __name__ == "__main__":
    test_topKFrequent()

