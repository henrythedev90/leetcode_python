const twoSum = (nums, target) => {
  let ref = {};
  for (let i = 0; i < nums.length; i++) {
    let difference = target - nums[i];
    if (ref[difference] !== undefined) {
      return [ref[difference], i];
    }
    ref[nums[i]] = i;
  }
};

const twoSumTwo = (nums, target) => {
  let ref = {};
  let i = 0;
  let arrayLength = nums.length;
  while (i < arrayLength) {
    let difference = target - nums[i];
    if (ref[difference] !== undefined) {
      return [ref[difference], i];
    }
    ref[nums[i]] = i;
    i++;
  }
};

nums = [2, 7, 11, 15];
target = 26;
let result = twoSumTwo(nums, target);
console.log(result);
