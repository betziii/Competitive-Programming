class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        check = defaultdict(set)
        answer = [[] for i in range(n)]
        indegrees = [0] * n
        for x,y in edges:
            graph[x].append(y)
            indegrees[y] += 1
        # print(graph, indegrees)
        
        q = deque()
        
        for i, val in enumerate(indegrees):
            if val == 0:
                q.append(i)
        # print(q)
        while q:
            node = q.popleft()
            for nei in graph[node]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    q.append(nei)
                for j in answer[node]:
                    check[nei].add(j)
                # print(check)
                check[nei].add(node)
                answer[nei] = list(set(answer[nei] + list(check[nei])))
                
                # print(q)
        # print(answer)
        for i in range(len(answer)):
            answer[i] = sorted(answer[i])
        return answer
        
            
        