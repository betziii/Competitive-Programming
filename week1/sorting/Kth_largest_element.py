class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums.sort(key = int)
        return nums[len(nums)-k]
        # for i in range(len(nums)-1):
        #     for j in range(0,len(nums)-i-1):
        #         if int(nums[j+1]) < int(nums[j]):
        #             nums[j], nums[j+1] = nums[j+1], nums[j]
        
        # for i in range(len(nums)-2):
        #     if int(nums[i]) == int(nums[i+1]):
        #         nums.remove(nums[i])

        
            