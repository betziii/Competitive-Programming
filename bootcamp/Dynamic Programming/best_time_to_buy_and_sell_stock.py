from ast import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        profit = 0
        for price in prices:
            profit = max(price - minimum, profit)
            minimum = min(price, minimum)
        return profit