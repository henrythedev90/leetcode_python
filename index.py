from typing import List

# def encode(strs: List[str]) -> str:
#     single_string = ""
#     for single_str in strs:
#         single_string += str(len(single_str))+ "#" + single_str
#     return single_string

# def decode(s: str) -> List[str]:
#     decoded_list = []
#     hash_index = 0
#     while hash_index < len(s):
#         hash_index = s.find("#", hash_index)
#         if hash_index == -1:
#             break
#         length = int(s[:hash_index])
#         decoded_list.append(s[hash_index+1:hash_index+1+length])
#         hash_index += 1
#     return decoded_list

# print(decode("3#abc#4#code"))

# Eights Out!Given an array of integers, remove all occurrences of neighboring elements that add up 8. If the removal 
# of two integers creates a new pair that adds to 8, remove those elements as well. 
# Example 1:
# Input: [1,2,3,5,6,9]

# Output: [1, 9]
#            Explanation: 3 and 5 = 8 so we remove them. Our new array [1,2,6,9] has 2 and 6 which equal 8, so we remove 
# this pair. We are left with [1, 9] they add up to 10 so they can stay.
# Example 2:
# Input: [1, 7]
# Output: []
# Explanation: 1 and 7 add up to 8 so both integers are removed leaving an empty array.
# Example 3:
# Input: [1, 6]
# Output: [1, 6]



# def remove_eight(nums:List[int]) -> List[int]:
#     new_array = []
#     for i in range(len(nums)):
#         if len(new_array) == 0:
#             new_array.append(nums[i])
#         elif len(new_array) > 0:
#             last_element = new_array[-1]
#             if last_element + nums[i] == 8:
#                 new_array.pop()
#             else:
#                 new_array.append(nums[i])
    
#     return new_array

# print(remove_eight([1,2,3,5,6,9]))
# print(remove_eight([1,7]))
# print(remove_eight([1,6]))


def subarraySum(nums:List[int], k:int) -> int:
    total = 0
    current = 0
    result = {0:1}
    for num in nums:
        current += num
        num_needed = current - k
        if num_needed in result:
            total += result[num_needed]
        result[current] = result.get(current, 0) + 1
    return result