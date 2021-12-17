from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ls = []
        result = [True]*len(l)
        for i in range(len(l)):
            ls.append(nums[l[i]:r[i]+1])
            ls[i].sort()
        
        
        for i in range(len(ls)):
            for j in range(2,len(ls[i])):
                sub = ls[i][1] - ls[i][0]
                if ls[i][j] - ls[i][j-1] != sub:
                    result[i] = False
        return result   
                