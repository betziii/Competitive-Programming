class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = [0] * 101
        for i in nums:
            n[i] += 1
        for i in range(1, 101):
            n[i] += n[i - 1]
        ans = []
        for i in nums:
            if i == 0:
                ans.append(0)
            else:
                ans.append(n[i - 1])
        
        return ans