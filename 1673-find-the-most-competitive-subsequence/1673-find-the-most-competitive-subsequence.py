class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
#         stack = []
#         i = 1
#         count = 0
        
#         for i in range(len(nums)): 
#             if len(stack) == 0:
#                 stack.append(nums[i])
#             else:
#                 while nums[i] < stack[-1] and i < len(nums)-1:
#                     stack.pop()
#                 stack.append(nums[i])
#             count += 1
#         return stack
        N = len(nums)
        stack = []
        for i, n in enumerate(nums):
            nums_left = N - i
            while stack and stack[-1] > n and nums_left > k - len(stack):
                stack.pop()
            if len(stack) < k:
                stack.append(n)
        return stack
            