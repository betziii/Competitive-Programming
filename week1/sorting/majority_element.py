class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = dict()
        res = []
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        for i in count:
            if count[i] > len(nums)//3:
                res.append(i)
        
        return res