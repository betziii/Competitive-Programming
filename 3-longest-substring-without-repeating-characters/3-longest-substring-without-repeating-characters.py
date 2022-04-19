class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        slow = 0
        fast = 0
        long = 0
        
        while slow <= fast and fast < len(s):
            if s[fast] not in visited:
                visited.add(s[fast])
             
            else:
                long = max(long, fast - slow)
                while s[slow] != s[fast]:
                    visited.remove(s[slow])
                    slow += 1
                slow +=1
            fast +=1
        return max(long, fast - slow)