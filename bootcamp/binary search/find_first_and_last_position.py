class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.search(nums,target,True)
        last = self.search(nums,target,False)
        return [first,last]
          
        
        
        
    def search(self,nums,target,flag): 
        left = 0
        right = len(nums)-1
        best = -1
        
        while(left <= right):
            mid = left + ((right - left)//2)
            if(nums[mid] > target):
                right = mid - 1
            elif(nums[mid] < target):
                left = mid + 1
            else:
                best = mid
                if flag == True:
                    right = mid - 1
                else:
                    left = mid + 1
                    
                
        return best