class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        j = len(nums)-1
        ls =[]
        while i <len(nums)//2 and i<j:
            ls.append(nums[i] + nums[j])
            i+=1
            j-=1
        return max(ls, default = 0)
            
        