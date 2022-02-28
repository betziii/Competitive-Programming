from ast import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l = 0 
        r = n - 1
        h = 0
        
        while l<=r:
            mid = l + (r-l)//2
            possibleH = n - mid
            if citations[mid]>= possibleH:
                h =  possibleH
                r = mid - 1
            else:
                l = mid + 1
                
        return h