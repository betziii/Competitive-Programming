class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 10//2   2**5 * 2**5
        # 5 //2   4 * 4 *2 = 2 ** 5  2 2 1 x**2 * x**2 * x = x ** 5 -> half * half * x
        # 2 //2   x ** 2  = 4  -> half
        # 1       2**1 2 -> half
        # 2 ** 2 2**2 2
        
        result = self.helper(x, abs(n))
        if n < 0:
            return 1/result
        return result
    def helper(self, x, n):
        if n == 1:
            return x
        if n == 0:
            return 1
        half = self.helper(x, n//2)
        if n % 2 == 0:
            return half * half
        return half * half * x
        