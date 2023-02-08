class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (x, y), val in zip(equations, values):
            graph[x][y] = val
            graph[y][x] = 1.0 / val
        
        def dfs(x, y, visited):
            if x not in graph or y not in graph:
                return -1.0
            if y in graph[x]:
                return graph[x][y]
            for i in graph[x]:
                if i not in visited:
                    visited.add(i)
                    temp = dfs(i, y, visited)
                    if temp == -1:
                        continue
                    else:
                        return graph[x][i] * temp
            return -1
        result = []
        for q in queries:
            result.append(dfs(q[0], q[1], set()))
        return result
        
