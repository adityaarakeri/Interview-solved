"""
121. Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""
from typing import List

def maxProfit(prices: List[int]) -> int:       
        # init left and right pointers 
        l = 0
        r = 1
        # profit starts at 0
        max_profit = 0

        while r < len(prices):
            # regular check if profit
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                # get the max profit and store
                max_profit = max(max_profit, profit)
            else:
                # we found a price lower than previos low
                l  = r
            # right moves as usual every iter
            r += 1

        return max_profit

q1 = [7,1,5,3,6,4]
q2 = [7,6,4,3,1]
print(maxProfit(q1))
print(maxProfit(q2))
