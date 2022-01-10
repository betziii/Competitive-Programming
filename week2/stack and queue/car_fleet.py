from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = len(position)
        pos = {}
        time = []
        for i in range(res):
            pos[position[i]] = speed[i]
        # print(pos)
        p = list(pos.items())
        p.sort(reverse=True)
        
        pos = dict(p)
        # print(pos)
        
        for v in pos:
            time.append((target - v)/pos[v])
        
        maxS = time[0]
        
        for i in range(1,len(time)):
            if time[i] <= maxS:
                res -= 1
            else:
                maxS = time[i]
            
            
        return res
