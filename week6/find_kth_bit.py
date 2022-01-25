class Solution:
    def bits(self,n):
        bitss = ""
        if n == 1:
            return "0"
        else:
            bitss = self.bits(n-1)
            result = bitss + "1" + self.reverse(self.invert(bitss))
            return result
        
    def reverse(self,x):
        return x[::-1]
    def invert(self,a):
        inverse = ''.join(['1' if i == '0' else '0'
                     for i in a])
        return inverse
        
    def findKthBit(self, n: int, k: int) -> str:
        res = self.bits(n)
        return res[k-1]
        # if n == 1:
        #     return "0"
        # else:
        #     bits = self.findKthBit(n-1,k)
        #     result = bits + "1" + str(reverse(invert(bits)))
        #     return result
    
        
        
        