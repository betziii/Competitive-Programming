class State:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, __o: object):
        return isinstance(__o, State) and self.x == __o.x and self.y == __o.y

    def __hash__(self):
        return hash(f'{self.x} {self.y}')    

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        visited = set()
        dirc = [(0,1), (1,0), (-1,0), (0,-1)]
        
        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        def dfs(row, col):
            count = 0
            side = 0
            
            for dr, dc in dirc:
                newr = row + dr
                newc = col + dc
                
                if not inbound(newr, newc) or grid[newr][newc] == 0:
                    side += 1
                    continue
                new_state = State(newr, newc)
                if new_state not in visited:
                    visited.add(new_state)
                    count += dfs(newr, newc)
            return side + count

                # if (newr,newc) not in visited:
                #     visited.add((newr, newc))
                #     count += dfs(newr, newc)
                # print(side, count)
                # return side + count
            
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and (i, j) not in visited:
                    visited.add(State(i, j))
                    return dfs(i, j)
        return 0
            
                        
                    