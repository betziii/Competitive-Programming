class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n = list(set(nums))
        if len(n) < 3:
            return max(n)
        else:
            n.remove(max(n))
            n.remove(max(n))
            return max(n)
        
        
