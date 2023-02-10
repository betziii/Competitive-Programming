class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        dicts = collections.defaultdict(int)
        i1, i2 = [], []
        
        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    i1.append((i, j))
                if img2[i][j] == 1:
                    i2.append((i, j))
        
        
        result = 0
        for x in i1:
            for y in i2:
                t = (y[0] - x[0], y[1] - x[1])
                dicts[t] += 1
                result = max(result, dicts[t])
        
        return result
        
