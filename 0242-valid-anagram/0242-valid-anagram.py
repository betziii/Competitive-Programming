class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # anagram  nagaram
        s = sorted(s)
        t = sorted(t)
        
        if len(t) == len(s) and s == t:
            return True
        return False
          
                