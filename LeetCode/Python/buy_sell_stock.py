# LeetCode Array # 2: Best Time to Buy and Sell Stock II

# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

# Find and return the maximum profit you can achieve.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.
# Example 2:

# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
# Total profit is 4.
# Example 3:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
 

# Constraints:

# 1 <= prices.length <= 3 * 104
# 0 <= prices[i] <= 104


from typing import List


class Solution:
    def maxProfit(self, prices:List[int]) -> int:
        if len(prices) < 2:
            return 0
        elif len(prices) == 2:
            rise = prices[1] - prices[0]
            if rise > 0:
                return rise
            else:
                return 0
        profit = 0
        curr = 2
        rise = prices[1] - prices[0]
        local_minima = 0
        local_maxima = 0
        if rise > 0:
            is_slope_positive = True
            local_minima = prices[0]
        else:
            is_slope_positive = False
            local_maxima = prices[0]
        while curr < len(prices):
            rise = prices[curr] - prices[curr - 1]
            if rise > 0 and is_slope_positive == False:
                is_slope_positive = True
                local_minima = prices[curr - 1]
            elif rise <= 0 and is_slope_positive == True:
                is_slope_positive = False
                local_maxima = prices[curr - 1]
                profit = profit + (local_maxima-local_minima)
            else:
                curr += 1
        if is_slope_positive == True:
            local_maxima = prices[len(prices) - 1]
            profit = profit + (local_maxima-local_minima)
        return profit

s = Solution()
prices=[1,2,3,4,5]
print(s.maxProfit(prices))

