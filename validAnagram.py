# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

def validAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    dictionary = {}

    for letter in s:
        if letter not in dictionary:
            dictionary[letter] = 1
        else:
            dictionary[letter] += 1
    
    for char in t:
        if char not in dictionary:
            return False
        if dictionary[char] == 0:
            return False
        dictionary[char] -= 1
    
    return True

# Test cases
def test_validAnagram():
    # Test case 1: Example from problem description
    s1, t1 = "anagram", "nagaram"
    result1 = validAnagram(s1, t1)
    expected1 = True
    print(f"Test 1: s='{s1}', t='{t1}'")
    print(f"Expected: {expected1}, Got: {result1}")
    print(f"Pass: {result1 == expected1}")
    print()
    
    # Test case 2: Example from problem description
    s2, t2 = "rat", "car"
    result2 = validAnagram(s2, t2)
    expected2 = False
    print(f"Test 2: s='{s2}', t='{t2}'")
    print(f"Expected: {expected2}, Got: {result2}")
    print(f"Pass: {result2 == expected2}")
    print()
    
    # Test case 3: Edge case - empty strings
    s3, t3 = "", ""
    result3 = validAnagram(s3, t3)
    expected3 = True
    print(f"Test 3: s='{s3}', t='{t3}'")
    print(f"Expected: {expected3}, Got: {result3}")
    print(f"Pass: {result3 == expected3}")
    print()
    
    # Test case 4: Edge case - different lengths
    s4, t4 = "hello", "world"
    result4 = validAnagram(s4, t4)
    expected4 = False
    print(f"Test 4: s='{s4}', t='{t4}'")
    print(f"Expected: {expected4}, Got: {result4}")
    print(f"Pass: {result4 == expected4}")
    print()
    
    # Test case 5: Edge case - single characters
    s5, t5 = "a", "a"
    result5 = validAnagram(s5, t5)
    expected5 = True
    print(f"Test 5: s='{s5}', t='{t5}'")
    print(f"Expected: {expected5}, Got: {result5}")
    print(f"Pass: {result5 == expected5}")
    print()
    
    # Test case 6: Edge case - single characters different
    s6, t6 = "a", "b"
    result6 = validAnagram(s6, t6)
    expected6 = False
    print(f"Test 6: s='{s6}', t='{t6}'")
    print(f"Expected: {expected6}, Got: {result6}")
    print(f"Pass: {result6 == expected6}")
    print()
    
    # Test case 7: Edge case - repeated characters
    s7, t7 = "aab", "aba"
    result7 = validAnagram(s7, t7)
    expected7 = True
    print(f"Test 7: s='{s7}', t='{t7}'")
    print(f"Expected: {expected7}, Got: {result7}")
    print(f"Pass: {result7 == expected7}")
    print()
    
    # Test case 8: Edge case - case sensitivity
    s8, t8 = "Anagram", "nagaram"
    result8 = validAnagram(s8, t8)
    expected8 = False
    print(f"Test 8: s='{s8}', t='{t8}'")
    print(f"Expected: {expected8}, Got: {result8}")
    print(f"Pass: {result8 == expected8}")
    print()
    
    # Test case 9: Edge case - numbers and special characters
    s9, t9 = "123!@#", "!@#123"
    result9 = validAnagram(s9, t9)
    expected9 = True
    print(f"Test 9: s='{s9}', t='{t9}'")
    print(f"Expected: {expected9}, Got: {result9}")
    print(f"Pass: {result9 == expected9}")
    print()
    
    # Test case 10: Edge case - spaces
    s10, t10 = "listen", "silent"
    result10 = validAnagram(s10, t10)
    expected10 = True
    print(f"Test 10: s='{s10}', t='{t10}'")
    print(f"Expected: {expected10}, Got: {result10}")
    print(f"Pass: {result10 == expected10}")
    print()
    
    # Test case 11: Edge case - palindrome
    s11, t11 = "racecar", "racecar"
    result11 = validAnagram(s11, t11)
    expected11 = True
    print(f"Test 11: s='{s11}', t='{t11}'")
    print(f"Expected: {expected11}, Got: {result11}")
    print(f"Pass: {result11 == expected11}")
    print()
    
    # Test case 12: Edge case - same string
    s12, t12 = "python", "python"
    result12 = validAnagram(s12, t12)
    expected12 = True
    print(f"Test 12: s='{s12}', t='{t12}'")
    print(f"Expected: {expected12}, Got: {result12}")
    print(f"Pass: {result12 == expected12}")
    print()

if __name__ == "__main__":
    test_validAnagram()

