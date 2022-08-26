# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

def maxProfit(prices):

    # create 2 pointes
    l = 0  # buy
    r = 1  # sell
    max_profit = 0

    # while the sell(right) pointer doesnt get to the end of the array:
    while r < len(prices):
        # if the price of the sell(right) pointer is greater than the buy(left) pointer,
        # store the profit (difference between them) and check if profit is greater than
        # the max_profit, if its, the max_profit will now be the profit
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            max_profit = max(profit, max_profit)
        # if the price of the sell is not grater than the buy, move the buy(left) pointer to
        # where the sell(right) pointer is
        else:
            l = r
        r += 1
    return max_profit


print(maxProfit([7, 1, 5, 3, 6, 4]))  # -> 5
