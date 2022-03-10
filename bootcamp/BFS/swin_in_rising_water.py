from ast import List
import heapq


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        queue = []
        heapq.heappush(queue, [grid[0][0] ,0, 0])
        
        visited = set()
        directional = [[0,1],[0,-1],[1,0],[-1,0]]
        maximum = 0
        while queue:
            val = heapq.heappop(queue)
            visited.add((val[1], val[2]))
            
            
            maximum = max(grid[val[1]][val[2]], maximum)
                
            for direction in directional:
                row = val[1] + direction[0]
                column = val[2] + direction[1]
                
                if (row < 0 or column < 0 or row >= len(grid) or column >= len(grid[0])):
                    continue
                    
                if (row, column) not in visited:
                    heapq.heappush(queue, [grid[row][column], row, column])
                    
            if grid[val[1]][val[2]] == grid[len(grid)-1][len(grid[0])-1]:
                return maximum