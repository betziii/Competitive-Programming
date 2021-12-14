class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ls = []
        lis = []
        dicts = {}
        for i in points:
            dis = ((i[0])**2 + (i[1])**2)
            if dis not in dicts:
                dicts[dis] = []
            
            dicts[dis].append(i)
        
        for i in sorted (dicts) :
            if k == 0: break
            for j in dicts[i]:
                if k>0:
                    ls.append(j)
                    k-=1
        
        return ls
        