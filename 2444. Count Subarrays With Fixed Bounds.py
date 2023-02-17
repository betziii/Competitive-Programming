class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        result = 0
        j = -1
        pMinKIdx = -1
        pMaxKIdx = -1

        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                j = i
            if num == minK:
                pMinKIdx = i
            if num == maxK:
                pMaxKIdx = i
            result += max(0, min(pMinKIdx, pMaxKIdx) - j)

        return result
