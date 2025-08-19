const maxArea = (height) => {
  let left = 0;
  let right = height.length - 1;
  let maxima = 0;

  while (left < right) {
    let width = right - left;
    let maxArea = Math.min(height[left], height[right]) * width;
    maxima = Math.max(maxima, maxArea);
    if (height[left] <= height[right]) {
      left++;
    } else {
      right--;
    }
  }
  return maxima;
};

let height = [1, 8, 6, 2, 5, 4, 8, 3, 7];
let heightTwo = [1, 1];
let result = maxArea(heightTwo);
console.log(result);
