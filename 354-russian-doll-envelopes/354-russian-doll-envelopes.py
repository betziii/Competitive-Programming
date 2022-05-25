from bisect import bisect_left as binary_search
class Problem300:
    def lengthOfLIS(self, nums: List[int]) -> int:
        array = [nums[0]]
        
        for num in nums[1:]:
            if num > array[-1]:
                array.append(num)
            else:
                index = binary_search(array, num)
                array[index] = num
                
        return len(array)
    
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        sorted_array = sorted(envelopes, key=lambda e: (e[0], -e[1]))
        return Problem300().lengthOfLIS([e[1] for e in sorted_array])