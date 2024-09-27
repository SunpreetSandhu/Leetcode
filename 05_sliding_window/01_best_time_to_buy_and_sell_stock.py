'''
Intuition:
The goal is to find the maximum profit you can achieve by buying the stock
one day and selling one day in future. We can use two pointer algorithm
We need to find the lowest combination by subtracting the sell day price and buy day price. 
If the sell day is less than buy day we will change the buy day to the sell day. 

Approach:
1) Return immediatly if the input array is less than length 2, since you cant buy and sell on a 1 day input (day)
2) Initialize 2 variables L (left, buy var), and profit (max profit) initially set to 0
3)Iterate through prices array with R (right, sell var), starting at index 1 (you cant sell and buy same day)
    a)If the price on day R is less than L, update L to R, as we found a new min val
    b)If the price on day R is greater than L, check the potential profit by doing prices[R]-prices[L] and update profit if this value is greater than current profit
4) return the final profit value, if no profit was found we return 0

Time Complexity:
O(n): n is the length of the prices array as we loop through it once

Space Complexity:
O(1): only simple variable declerations, no variable that scales with input

'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        L = 0
        profit = 0
        for R in range (1, len(prices)):
            if prices[R]-prices[L] <= 0:
                L = R
            else:
                profit = max(prices[R] - prices[L], profit)
        return profit


        