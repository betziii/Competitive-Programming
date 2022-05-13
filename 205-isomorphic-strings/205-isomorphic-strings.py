class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapS_T = {}
        mapT_S = {}
        
        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]
            
            if ((c1 in mapS_T and mapS_T[c1] != c2) or (c2 in mapT_S and mapT_S[c2] != c1)):
                return False
            mapS_T[c1] = c2
            mapT_S[c2] = c1
        return True