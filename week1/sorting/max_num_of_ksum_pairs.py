class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        print(nums)
        # n = len(nums)
        j = 0
        i = len(nums)-1
        count = 0
        while j<i:
            if nums[i] + nums[j] == k:
                # print("if", i)
                i -=1
                j +=1
                count +=1 
            elif nums[i] + nums[j] > k:
                # print("elif", i)
                i -=1
                
            else:
                j +=1
                
        return count