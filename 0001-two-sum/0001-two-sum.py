class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap = value:index
        # if target - nums[i] exists in hashmap
        # if it doesn't exist we add the nums[i] to the hashmap
        previous = {}
        
        for i in range(len(nums)):
            a = target - nums[i]
            if a in previous:
                return [previous[a], i]
            previous[nums[i]] = i
        
        
                
                
        
        
        