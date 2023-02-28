class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix: 
            return 0
        r = len(matrix)
        c = len(matrix[0])
        dp = [[0]*c for _ in range(r)]
        mx_count = 0
        for i in range(r):
            for j in range(c):
                dp[i][j] = int(matrix[i][j])
                if dp[i][j]: mx_count = 1
        for i in range(1,r):
            for j in range(1,c):
                if dp[i][j] and dp[i-1][j] and dp[i][j-1] and dp[i-1][j-1]:
                    dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
                    mx_count = dp[i][j] if dp[i][j]>mx_count else mx_count
        return mx_count**2
