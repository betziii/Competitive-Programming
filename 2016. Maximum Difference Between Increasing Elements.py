class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res = -1
        m = nums[0]

        for i in range(len(nums)):
            if nums[i] > m:
                res = max(res, nums[i] - m)
            m = min(m, nums[i])

        return res
