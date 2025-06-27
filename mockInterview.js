// First Elements Occurring K Times in an Array
// Given an array and an integer k, return the first element that occurs at least k times.

// Example
// Input [3,4,1,5,4,2,3,5,3,4]
// Output: k =2 => 4, k = 3 => 3

// Follow-Up
// What about if we wanted the first element occurring exactly k times.

// Example
// Input [3,4,1,5,4,2,3,5,3,4]
// Output: k = 2 => 5, k = 3 => 3

const occursKTimes = (arr, k) => {
  let checker = {};
  for (let i = 0; i < arr.length; i++) {
    if (!checker[arr[i]]) {
      checker[arr[i]] = 1;
    } else {
      checker[arr[i]]++;
    }
  }
  for (let key in checker) {
    if (checker[key] === k) {
      return key;
    }
  }
};
console.log(occursKTimes([3, 4, 1, 5, 4, 2, 3, 5, 3, 4], 2));
