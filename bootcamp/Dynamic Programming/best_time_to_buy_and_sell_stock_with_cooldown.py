from ast import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dicts = {}
#         bs : buy sell boolean if true buy if false sell
        def dfs(i, bs):
            if i >= len(prices):
                return 0
            if (i,bs) in dicts:
                return dicts[(i,bs)]
            cooldown = dfs(i + 1, bs)
            if bs:
                buy = dfs(i + 1, not bs) - prices[i]
                dicts[(i, bs)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not bs) + prices[i]
                dicts[(i, bs)] = max(sell, cooldown)
            return dicts[(i, bs)]
        return dfs(0, True)