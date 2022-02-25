# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        result = 1
        
        while left <= right:
            mid = left + (right - left)//2
          
            if isBadVersion(mid) == True:
                right = mid - 1
                result = mid
            else:
                left = mid + 1
        return result
                
                