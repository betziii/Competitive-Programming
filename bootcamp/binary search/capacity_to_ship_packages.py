class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        while l <= r:
            mid = (l + r) // 2
            if not self.isValid(weights, days, mid):
                l = mid + 1
            else:
                r = mid - 1
        return l
    
    def isValid(self, weights, days, size):
        sums = 0
        for i in weights:
            sums += i
            if sums > size:
                days -= 1
                sums = i
                if days == 0:
                    break
        return days > 0