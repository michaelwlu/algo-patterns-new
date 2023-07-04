// find the maximum profit that you can gain by buying the stock once and then selling it
// if no profit can be made, return 0
export function maxProfit(stockPrices) {
	let buyIndex = 0;
	let maxProfit = 0;

	for (let sellIndex = 1; sellIndex < stockPrices.length; sellIndex++) {
		const currProfit = stockPrices[sellIndex] - stockPrices[buyIndex];

		if (currProfit > 0) {
			maxProfit = Math.max(maxProfit, currProfit);
		} else {
			buyIndex = sellIndex;
		}
	}

	return maxProfit;
}
