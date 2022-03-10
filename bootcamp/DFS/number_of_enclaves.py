class Solution:
    def dfs(self,grid, row, col, flag):
        self.visited.add((row, col))
        for d in self.direction:
            new_row = row + d[0]
            new_col = col + d[1]
            
            if self.in_bound(new_row, new_col) and grid[new_row][ new_col] == 1 and (new_row, new_col) not in self.visited:
                self.dfs(grid, new_row, new_col, flag)
        if flag:
            self.count += 1
            # board[row][col] = 'X'
    def numEnclaves(self, grid: List[List[int]]) -> int:
        self.direction = [(0,1), (1,0), (0,-1), (-1,0)]
        m = len(grid)
        n = len(grid[0])
        self.count = 0
        self.visited = set()
        self.in_bound = lambda row, col: 0 <= row < m and 0 <= col < n
        
        for i in range(m):
            if grid[i][0] == 1 and (i,0) not in self.visited:
                self.dfs(grid, i, 0, False)
        for j in range(n):
            if grid[0][j] == 1 and (0,j) not in self.visited:
                self.dfs(grid, 0, j, False)
        for k in range(m):
            if grid[k][n-1] == 1 and (k,n-1) not in self.visited:
                self.dfs(grid, k, n-1, False)
        for l in range(n):
            if grid[m-1][l] == 1 and (m-1,l) not in self.visited:
                self.dfs(grid, m-1, l, False)
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1 and (row, col) not in self.visited:
                    self.dfs(grid, row, col, True)
        return self.count