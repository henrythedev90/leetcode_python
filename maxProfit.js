const maxProfit = (prices) => {
  let currentMin = prices[0];
  let currentMax = 0;
  let i = 0;
  let pricesLength = prices.length;

  while (i < pricesLength) {
    if (prices[i] < currentMin) {
      currentMin = prices[i];
    }
    let profit = prices[i] - currentMin;
    if (currentMax < profit) {
      currentMax = profit;
    }
    i++;
  }

  return currentMax;
};

let prices = [7, 1, 5, 3, 6, 4];
let result = maxProfit(prices);
console.log(result);
