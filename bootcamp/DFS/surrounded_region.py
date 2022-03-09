class Solution:
    def dfs(self,board, row, col, flag):
        self.visited.add((row, col))
        for d in self.direction:
            new_row = row + d[0]
            new_col = col + d[1]
            
            if self.in_bound(new_row, new_col) and board[new_row][ new_col] == 'O' and (new_row, new_col) not in self.visited:
                self.dfs(board, new_row, new_col, flag)
        if flag:
            board[row][col] = 'X'
    
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.direction = [(0,1), (1,0), (0,-1), (-1,0)]
        m = len(board)
        n = len(board[0])
        self.visited = set()
        self.in_bound = lambda row, col: 0 <= row < m and 0 <= col < n
        
        for i in range(m):
            if board[i][0] == 'O' and (i,0) not in self.visited:
                self.dfs(board, i, 0, False)
        for j in range(n):
            if board[0][j] == 'O' and (0,j) not in self.visited:
                self.dfs(board, 0, j, False)
        for k in range(m):
            if board[k][n-1] == 'O' and (k,n-1) not in self.visited:
                self.dfs(board, k, n-1, False)
        for l in range(n):
            if board[m-1][l] == 'O' and (m-1,l) not in self.visited:
                self.dfs(board, m-1, l, False)
        for row in range(m):
            for col in range(n):
                if board[row][col] == 'O' and (row, col) not in self.visited:
                    self.dfs(board, row, col, True)
        