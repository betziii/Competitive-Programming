class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l = 1
        r = len(nums) - 1
        
        while l <= r:
            cur = (l + r) // 2
            count = 0
            count = sum(num <= cur for num in nums)
            if count > cur:
                dup = cur
                r = cur - 1
            else:
                l = cur + 1
        return dup
                