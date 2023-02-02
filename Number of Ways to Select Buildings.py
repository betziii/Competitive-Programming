class Solution:
    def numberOfWays(self, s: str) -> int:
        n = len(s)
        t = 0
        visited = [[0] * 2 for i in range(2)]
        for i in range(n):
            c = int(s[i])
            t += visited[1][1-c]
            visited[1][c] += visited[0][1-c]
            visited[0][c] += 1
        return t
