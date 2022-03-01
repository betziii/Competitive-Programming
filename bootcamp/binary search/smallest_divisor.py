import math

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, 1000000
        while l <= r:
            mid = l + (r-l)//2
            summ = 0
            for i in range(len(nums)):
                quotient = math.ceil(nums[i] / mid)
                summ += quotient
            
            if summ <= threshold:
                best = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return best