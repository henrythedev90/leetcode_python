var topKFrequent = function (nums, k) {
  let obj = {};

  for (let i = 0; i < nums.length; i++) {
    if (!obj[nums[i]]) {
      obj[nums[i]] = 1;
    } else {
      obj[nums[i]]++;
    }
  }

  let sortedEntries = Object.entries(obj)
    .sort((a, b) => b[1] - a[1])
    .slice(0, k)
    .map((entry) => Number(entry[0]));

  return sortedEntries;
};
nums = [1, 1, 1, 2, 2, 3];
k = 3;
let result = topKFrequent(nums, k);
console.log(result);
