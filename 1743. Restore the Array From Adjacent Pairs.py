class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
        cur = None
        for u in graph:
            if len(graph[u]) == 1:
                cur = u
                break
        result = []
        visited = set()
        while cur != None:
            result.append(cur)
            visited.add(cur)
            ns = graph[cur]
            cur = None
            
            for n in ns:
                if n not in visited:
                    cur = n
        return result
        
