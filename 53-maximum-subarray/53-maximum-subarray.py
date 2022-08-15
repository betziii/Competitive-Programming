class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxh = 0
        maxf = nums[0]
        for i in range(len(nums)):
            maxh += nums[i]
            if maxh < nums[i]:
                maxh = nums[i]
            if maxf < maxh:
                maxf = maxh
        return maxf