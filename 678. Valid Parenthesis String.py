class Solution:
    def dfs(self, s, idx, l, dp):
        if idx >= len(s) or l < 0:
            return l == 0 
        if dp[idx][l] != -1:
            return dp[idx][l]
        ans1 = ans2 = ans3 = False
        if s[idx] == '(':
            ans1 = self.dfs(s, idx + 1, l + 1, dp)
        elif s[idx] == ')':
            ans2 = self.dfs(s, idx + 1, l - 1, dp)
        elif s[idx] == "*":
            ans3 = (self.dfs(s, idx + 1, l + 1, dp) or self.dfs(s,idx + 1,l - 1, dp) or self.dfs(s, idx + 1, l, dp))
        dp[idx][l] = ans1 or ans2 or ans3
        return dp[idx][l]
            
        
    def checkValidString(self, s: str) -> bool:
        dp = [[-1 for i in range(len(s))] for j in range(len(s))]
        return self.dfs(s, 0, 0, dp)
        
