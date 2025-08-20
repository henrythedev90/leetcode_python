const lengthOfLongestSubstring = (str) => {
  let longestString = 0;
  let set = new Set();
  let left = 0;
  let right = 0;
  while (right < str.length) {
    let letter = str[right];
    if (!set.has(letter)) {
      set.add(letter);
      longestString = Math.max(longestString, set.size);
      right++;
    } else {
      set.delete(str[left]);
      left++;
    }
  }
  return longestString;
};

let letter = "henry";
let result = lengthOfLongestSubstring(letter);
console.log(result);
