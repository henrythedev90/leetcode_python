def lengthOfLongestSubstring(self, s: str) -> int:
    left = 0
    max_number = 0
    my_set = set()
    for right in range(len(s)):
        current_str = s[right]
        while current_str in my_set:
            my_set.remove(s[left])
            left += 1
        my_set.add(s[right])
        max_number = max(max_number, right - left + 1)
    return max_number

# Test cases
def test_lengthOfLongestSubstring():
    # Create an instance to call the method
    class Solution:
        def lengthOfLongestSubstring(self, s: str) -> int:
            return lengthOfLongestSubstring(self, s)
    
    solution = Solution()
    
    # Test case 1: Example from problem description
    s1 = "abcabcbb"
    result1 = solution.lengthOfLongestSubstring(s1)
    expected1 = 3  # "abc" with length 3
    print(f"Test 1: s='{s1}'")
    print(f"Expected: {expected1}, Got: {result1}")
    print(f"Pass: {result1 == expected1}")
    print()
    
    # Test case 2: Example from problem description
    s2 = "bbbbb"
    result2 = solution.lengthOfLongestSubstring(s2)
    expected2 = 1  # "b" with length 1
    print(f"Test 2: s='{s2}'")
    print(f"Expected: {expected2}, Got: {result2}")
    print(f"Pass: {result2 == expected2}")
    print()
    
    # Test case 3: Example from problem description
    s3 = "pwwkew"
    result3 = solution.lengthOfLongestSubstring(s3)
    expected3 = 3  # "wke" with length 3
    print(f"Test 3: s='{s3}'")
    print(f"Expected: {expected3}, Got: {result3}")
    print(f"Pass: {result3 == expected3}")
    print()
    
    # Test case 4: Edge case - empty string
    s4 = ""
    result4 = solution.lengthOfLongestSubstring(s4)
    expected4 = 0
    print(f"Test 4: s='{s4}'")
    print(f"Expected: {expected4}, Got: {result4}")
    print(f"Pass: {result4 == expected4}")
    print()
    
    # Test case 5: Edge case - single character
    s5 = "a"
    result5 = solution.lengthOfLongestSubstring(s5)
    expected5 = 1
    print(f"Test 5: s='{s5}'")
    print(f"Expected: {expected5}, Got: {result5}")
    print(f"Pass: {result5 == expected5}")
    print()
    
    # Test case 6: Edge case - all unique characters
    s6 = "abcdef"
    result6 = solution.lengthOfLongestSubstring(s6)
    expected6 = 6
    print(f"Test 6: s='{s6}'")
    print(f"Expected: {expected6}, Got: {result6}")
    print(f"Pass: {result6 == expected6}")
    print()
    
    # Test case 7: Edge case - repeating pattern
    s7 = "abcabcabc"
    result7 = solution.lengthOfLongestSubstring(s7)
    expected7 = 3  # "abc" with length 3
    print(f"Test 7: s='{s7}'")
    print(f"Expected: {expected7}, Got: {result7}")
    print(f"Pass: {result7 == expected7}")
    print()
    
    # Test case 8: Edge case - palindrome
    s8 = "racecar"
    result8 = solution.lengthOfLongestSubstring(s8)
    expected8 = 4  # "race" or "ecar" with length 4
    print(f"Test 8: s='{s8}'")
    print(f"Expected: {expected8}, Got: {result8}")
    print(f"Pass: {result8 == expected8}")
    print()
    
    # Test case 9: Edge case - numbers and special characters
    s9 = "123!@#"
    result9 = solution.lengthOfLongestSubstring(s9)
    expected9 = 6
    print(f"Test 9: s='{s9}'")
    print(f"Expected: {expected9}, Got: {result9}")
    print(f"Pass: {result9 == expected9}")
    print()
    
    # Test case 10: Edge case - spaces
    s10 = "hello world"
    result10 = solution.lengthOfLongestSubstring(s10)
    expected10 = 6  # "hello " or "o worl" with length 6
    print(f"Test 10: s='{s10}'")
    print(f"Expected: {expected10}, Got: {result10}")
    print(f"Pass: {result10 == expected10}")
    print()
    
    # Test case 11: Edge case - long string with repeating characters
    s11 = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    result11 = solution.lengthOfLongestSubstring(s11)
    expected11 = 26  # First 26 unique characters
    print(f"Test 11: s='{s11}'")
    print(f"Expected: {expected11}, Got: {result11}")
    print(f"Pass: {result11 == expected11}")
    print()
    
    # Test case 12: Edge case - alternating characters
    s12 = "ababababab"
    result12 = solution.lengthOfLongestSubstring(s12)
    expected12 = 2  # "ab" with length 2
    print(f"Test 12: s='{s12}'")
    print(f"Expected: {expected12}, Got: {result12}")
    print(f"Pass: {result12 == expected12}")
    print()
    
    # Test case 13: Edge case - substring at the end
    s13 = "abcdefgabcdefg"
    result13 = solution.lengthOfLongestSubstring(s13)
    expected13 = 7  # "abcdefg" with length 7
    print(f"Test 13: s='{s13}'")
    print(f"Expected: {expected13}, Got: {result13}")
    print(f"Pass: {result13 == expected13}")
    print()
    
    # Test case 14: Edge case - substring in the middle
    s14 = "abcdefghijklmnopqrstuvwxyz"
    result14 = solution.lengthOfLongestSubstring(s14)
    expected14 = 26  # All 26 characters are unique
    print(f"Test 14: s='{s14}'")
    print(f"Expected: {expected14}, Got: {result14}")
    print(f"Pass: {result14 == expected14}")
    print()

if __name__ == "__main__":
    test_lengthOfLongestSubstring()