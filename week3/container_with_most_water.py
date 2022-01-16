from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        i,j = 0,len(height)-1
        left,right = 0,len(height)-1
        
        while (i<j):
            # print(i,j,left,right, max_area)

            
            max_area = max(max_area, min(height[i],height[j]) * (j-i))
            
            
            if (height[j] < height[i]):
                
                j = right-1
                while (height[j] < height[right]):
                    j-=1

                right=j

                max_area = max(max_area, min(height[i],height[j]) * (j-i))
            
            else :
                i = left+1
                while (height[i] < height[left]):
                    i+=1

                left = i

                max_area = max(max_area, min(height[i],height[j]) * (j-i))
            

         
        return max_area