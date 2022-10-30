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
        for num in nums:
            if num in frequency:
                return True
            else:
                frequency[num] = 1
        return False
        