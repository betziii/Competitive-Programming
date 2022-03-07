class Solution:
    def isValid(self,grid,row,col):
        return  0 <= row < len(grid) and ( 0 <= col < len(grid[0])) 
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        maximum = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maximum = max(self.dfs(grid,i,j), maximum)
        if maximum <= 1:
            return maximum
        return maximum -1 
    
    def dfs(self, grid,row, col):
        
        directions = [(0,1), (1,0), (0, -1), (-1, 0)]
        if not grid[row][col]:
            return 0
        
        count = 1
        for dirc in directions:
            new_row, new_col = row + dirc[0], col + dirc[1]
            if self.isValid(grid,new_row, new_col) and grid[new_row][new_col] == 1:
                grid[new_row][new_col] = 2
                count += self.dfs(grid, new_row, new_col)
        return count
