class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(0, len(nums)-1):
            for j in range(0,len(nums)):
                if nums[i] == nums[j]:
                    if i < j:
                        count += 1
                    else:
                        continue
        return count
                