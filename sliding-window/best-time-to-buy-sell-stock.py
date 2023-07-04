# find the maximum profit that you can gain by buying the stock once and then selling it
# if no profit can be made, return 0
def max_profit(stock_prices):
    max_profit = 0
    buy_index = 0

    for sell_index in range(1, len(stock_prices)):
        curr_profit = stock_prices[sell_index] - stock_prices[buy_index]

        if curr_profit > 0:
            max_profit = max(max_profit, curr_profit)
        else:
            buy_index = sell_index

    return max_profit
