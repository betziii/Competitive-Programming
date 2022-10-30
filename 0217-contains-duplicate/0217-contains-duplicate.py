class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
#         [1,2,3,1]
#         1,1
#         true
#         dict
#         1: 2
#         2: 1
#         3: 1
#         []
            
#         dict value > 1 true
        frequency = dict()
        isDuplicate = False
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        for key in nums:
            if frequency[key] > 1:
                isDuplicate = True
        return isDuplicate
        