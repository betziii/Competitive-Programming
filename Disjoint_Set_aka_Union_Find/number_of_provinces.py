from ast import List


class Union_Find:
    def __init__(self,n):
        self.child = [1] * n
        self.parent = list(range(n))
        self.count = n
        
    def find(self, node):
            if node != self.parent[node]:
                return self.find(self.parent[node])
            return self.parent[node]
        
    def union(self, node1, node2):
        p1 = self.find(node1)
        p2 = self.find(node2)

        if p1 != p2:
            if self.child[p1] < self.child[p2]:
                self.parent[p1] = p2
                self.child[p2] += self.child[p1]
            elif self.child[p1] > self.child[p2]:
                self.parent[p2] = p1
                self.child[p1] += self.child[p2]
            else:
                self.parent[p2] = p1
            self.count -= 1
        
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        m = len(isConnected[0])
        uf = Union_Find(n)
       
        for i in range(n):
            for j in range(m):
                if i != j and isConnected[i][j]==1:
                    uf.union(i,j)
        return uf.count
        
        