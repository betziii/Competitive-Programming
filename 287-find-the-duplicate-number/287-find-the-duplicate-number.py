class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        bits = 0 
        for n in nums: 
            nbit = (bits >> n) & 1
            if nbit == 0:
                bits |= 1 << n
            else:
                return n
        return -1