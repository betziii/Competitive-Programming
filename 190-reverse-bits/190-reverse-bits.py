class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        m = 1
        for i in range(0,32):
            if n & m:
                res += 1
            if i != 31:
                res <<= 1
            m <<= 1
        return res