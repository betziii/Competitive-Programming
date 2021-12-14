class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        frequency =[0]*100
        n = len(nums)
        ptr = 0
        for i in range(0,n):
            frequency[nums[i]] +=1
        for i in range(len(frequency)):
            count = frequency[i]
            while (count):
                nums[ptr] = i
                ptr +=1
                count -=1
            
                