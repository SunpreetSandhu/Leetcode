'''
Intuition:
The problem is asking us to calculate the max profit from buying and selling a stock multiple times, given an array of prices where each element at index i represents the stock price on the i’th day. The goal is to maximize the profit by capturing all increases in price no matter how small. If the price increases from one day to the next we consider it a valid profit opportunity.

Approach:
1)Initialize a variable profit = 0
2)Loop from day 1 to the end of the prices list
    a)If the previous day’s price is less than or equal to the current day’s price, we will increment the profit to include the difference between these 2 days 
3)Return profit

Time Complexity: O(n) -> Iterate through the profit array, n represents the days
Space Complexity: O(1) -> No extra memory used apart from constant variables(profit)
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(1,len(prices)):
            if prices[i-1] <= prices[i]:
                profit += prices[i] - prices[i-1]
        return profit