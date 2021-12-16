from typing import Collection


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        dicts = Collection.Counter(changed)
        # print(dicts)
        result = []
        
        if (len(changed) % 2 != 0): return []
        else:
            for n in sorted(dicts.keys()):
                while (n == 0 and dicts[n] >= 2):             
                    dicts[n] -= 2
                    result.append(n)


                while (n > 0 and dicts[n] and dicts[n * 2]):
                    dicts[n] -= 1
                    dicts[n * 2] -= 1
                    result.append(n) 
                
        
        return result if len(changed)//2 == len(result) else []
        
        # for i in dicts:
        
        
                
       
            