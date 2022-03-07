from ast import List


class Solution:
    def __init__(self):
        self.similar = {}
    def minJumps(self, arr: List[int]) -> int:
        for i in range(len(arr)):
            if arr[i] not in self.similar.keys():
                self.similar[arr[i]] = []
            self.similar[arr[i]].append(i)
            
        return self.BFS(arr)
        
    def BFS(self, arr):
        queue = deque()
        queue.append(0)
        visited = set()
        
        level = 0
        while queue:         
            for i in range(len(queue)):
                val = queue.popleft()   
                visited.add(val)
                if val == len(arr) - 1:
                    return level
                
                for n in self.similar[arr[val]]:
                    if (n not in visited):
                        queue.append(n)
                self.similar[arr[val]] = [] 
                if ((val - 1 >= 0 and val - 1 < len(arr)) and (val - 1 not in visited)):
                    queue.append(val - 1)
                if ((val + 1 < len(arr) and val + 1 >= 0) and (val + 1 not in visited)):
                    queue.append(val + 1)              
                
                    
            level += 1
        
        return level