class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(k) for k in version1.split('.')]
        v2 = [int(k) for k in version2.split('.')]
        
        i = 0
        while i < len(v1) or i < len(v2):
            a = v1[i] if i < len(v1) else 0
            b = v2[i] if i < len(v2) else 0
            if a < b:
                return -1
            elif a > b:
                return 1
            i += 1
        return 0