class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
                    
        intervals = sorted(intervals, key = lambda x: x[0])
        ls = []
        for i in intervals:
            if ls and max(ls[-1]) >= min(i):
                l = ls.pop()
                ls.append([min(min(i),min(l)), max(max(i), max(l))])
            else:
                ls.append(i)
        return ls
              
                    
       