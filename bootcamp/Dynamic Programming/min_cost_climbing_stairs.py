from ast import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        self.f = [0] * n
        return min(self.dp(cost, n-1), self.dp(cost, n-2))
    def dp(self, cost, n):
        if n < 0:
            return 0
        if n == 0 or n == 1:
            return cost[n]
        elif self.f[n] != 0:
            return self.f[n]
        else:
            self.f[n] = cost[n] + min(self.dp(cost,n-1), self.dp(cost, n-2))
        return self.f[n]