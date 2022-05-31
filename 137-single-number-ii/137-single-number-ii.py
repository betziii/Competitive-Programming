class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        carry = sum_n = 0
        for n in nums:
            carry, sum_n = sum_n & n | carry & ~n, (sum_n ^ n) & ~carry
        return carry | sum_n