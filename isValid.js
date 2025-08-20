// 20. Valid Parentheses
// Easy
// Topics
// premium lock icon
// Companies
// Hint
// Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

// An input string is valid if:

// Open brackets must be closed by the same type of brackets.
// Open brackets must be closed in the correct order.
// Every close bracket has a corresponding open bracket of the same type.

// Example 1:

// Input: s = "()"

// Output: true

// Example 2:

// Input: s = "()[]{}"

// Output: true

// Example 3:

// Input: s = "(]"

// Output: false

// Example 4:

// Input: s = "([])"

// Output: true

// Example 5:

// Input: s = "([)]"

// Output: false

// Constraints:

// 1 <= s.length <= 104
// s consists of parentheses only '()[]{}'.

const isValid = (s) => {
  let obj = { "(": ")", "[": "]", "{": "}" };
  let ref = [];
  for (const char of s) {
    if (obj[char]) {
      ref.push(char);
    } else {
      let popped = ref.pop();
      if (obj[popped] !== char) {
        return false;
      }
    }
  }
  return ref.length === 0;
};

let input = "()[]()[}";
let result = isValid(input);
console.log(result);
