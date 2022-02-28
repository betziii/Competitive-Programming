"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        result = []
        for i in range(1, z+1):
            ans = -1
            l = 1
            r = z
            while l <= r:
                mid = l + (r-l)//2
                # print(mid)
                if customfunction.f(i,mid) < z:
                    l = mid + 1
                elif customfunction.f(i,mid) > z:
                    r = mid - 1
                else:
                    ans = mid
                    break
                   
            if ans != -1:
                result.append([i,ans])
        return result