from ast import List
from collections import deque


class Solution:
    def isValid(self,grid,row,col):
        return  0 <= row < len(grid) and ( 0 <= col < len(grid[0])) 
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        count = 0
        direction = ((0,1),(0,-1),(-1,0),(1,0))
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    
                    q.append((row,col,count))
        while q:
            row, col, count = q.popleft()
            for r, c in direction:
                new_row = row + r
                new_col = col + c
                if self.isValid(grid,new_row,new_col) and grid[new_row][new_col] == 1 :
                    grid[new_row][new_col] = 2
                    q.append((new_row, new_col, count+1))
            
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return -1
               
        return count