class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        length = len(nums)
        memo = [[-1]* 1001 for _ in range(20)]
        answer = self.helper(0, 0, target, memo, length, nums)
        return answer
        
    def helper(self, current_index, current_sum, target, memo, length,nums):
        if current_index == length:
            if current_sum == target:
                return 1
            return 0
        if memo[current_index][current_sum] != -1:
            return memo[current_index][current_sum]
        positive = self.helper(current_index + 1,current_sum + nums[current_index],target, memo, length, nums)
        negative = self.helper(current_index + 1,current_sum - nums[current_index],target, memo, length, nums)
        
        answer = positive + negative
        memo[current_index][current_sum] = answer
        
        return answer