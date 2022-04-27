class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        parent = [i for i in range(n)]
        edges = []
        min_cost = 0
        
        
        for curr in range(n):
            for nextt in range(curr + 1, n):
                cost = abs(points[curr][0] - points[nextt][0]) + abs(points[curr][1] - points[nextt][1])
                edges.append((cost, curr, nextt))
        edges.sort()
        
        def find(node):
            if node != parent[node]:
                parent[node] = find(parent[node])
            return parent[node]
        def union(node1, node2):
            p1 = find(node1)
            p2 = find(node2)
            
            if p1 != p2:
                parent[p2] = p1
                return True
            return False
        for cost, node1, node2 in edges:
            if union(node1, node2):
                min_cost += cost
        return min_cost