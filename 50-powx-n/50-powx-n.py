class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = self.helper(x, abs(n))
        
        if n < 0:
            return 1/res
        return res
    
    def helper(self, x, n):
        if n == 1:
            return x
        if n == 0:
            return 1
        half = self.helper(x, n // 2)
        if n % 2 == 0:
            return half * half
        return half * half * x