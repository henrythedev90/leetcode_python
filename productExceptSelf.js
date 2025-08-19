const productExceptSelf = (arr) => {
  let arrLength = arr.length;
  let result = new Array(arrLength).fill(1);
  let startOne = 1;
  for (let i = 0; i < arr.length; i++) {
    result[i] = startOne;
    startOne *= arr[i];
  }
  let startTwo = 1;
  for (let i = arr.length - 1; i >= 0; i--) {
    result[i] *= startTwo;
    startTwo *= arr[i];
  }
  return result;
};

const productExceptSelfTwo = (arr) => {
  let forward = [];
  let startOne = 1;
  for (let i = 0; i < arr.length; i++) {
    forward.push(startOne);
    startOne *= arr[i];
  }
  let backward = [];
  let startTwo = 1;
  for (let i = arr.length - 1; i >= 0; i--) {
    backward.unshift(startTwo * forward[i]);
    startTwo *= arr[i];
  }
  return backward;
};
let testArr = [1, 2, 3, 4];
let testRes = productExceptSelfTwo(testArr);
let testResAgain = productExceptSelf(testArr);
console.log(JSON.stringify(testRes) === JSON.stringify(testResAgain));
