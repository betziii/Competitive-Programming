class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        left = 1
        right = 1
        n = len(nums)
        
        for i in range(0, n):
            ans[i] *= left
            ans[-1-i] *= right
            # print(ans)
            left *= nums[i]
            right *= nums[-1-i]
        return ans
        
            
        
            