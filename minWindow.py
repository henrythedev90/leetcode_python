from collections import Counter, defaultdict
# 76. Minimum Window Substring
# Hard
# Topics
# premium lock icon
# Companies
# Hint
# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

 

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.

def minWindow(s: str, t: str) -> str:
    if not t or not s:
        return ""
    
    t_freq = Counter(t)
    required_len = len(t_freq)
    window_count = defaultdict(int)
    left = 0
    formed_char = 0
    min_len = float('inf')
    min_start_index = 0

    for right in range(len(s)):
        char_r = s[right]
        window_count[char_r] += 1
        if char_r in t_freq and window_count[char_r] == t_freq[char_r]:
            formed_char += 1
        while formed_char == required_len:
            current_window = right - left + 1
            if current_window < min_len:
                min_len = current_window
                min_start_index = left
            
            char_l = s[left]
            window_count[char_l] -= 1

            if char_l in t_freq and window_count[char_l] < t_freq[char_l]:
                formed_char -= 1
            
            left += 1
    
    if min_len == float("inf"):
        return ""
    else:
        return s[min_start_index : min_start_index + min_len]



# Test cases
print(minWindow("ADOBECODEBANC", "ABC"))  # Expected: "BANC"
print(minWindow("a", "a"))  # Expected: "a"
print(minWindow("a", "aa"))  # Expected: ""