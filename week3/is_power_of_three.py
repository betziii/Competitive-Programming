class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n % 3 != 0 and n != 1 or n<=0:
            return False
        elif n == 1:
            # n = n//3
            return True
        return self.isPowerOfThree(n//3)