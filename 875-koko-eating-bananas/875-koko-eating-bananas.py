import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = max(piles)
        best = k
        
        def eater(k):
            hrs = h
            for pile in piles:
                hrs -= math.ceil(pile / k)
            return hrs
        
        l = 1
        r = k
        while l <= r:
            mid = l + (r - l)//2
            if eater(mid) < 0:
                l = mid + 1
            else:
                r = mid - 1
                best = mid
        return best
            
            
            
            

                    
                    
                
        
        
        
        