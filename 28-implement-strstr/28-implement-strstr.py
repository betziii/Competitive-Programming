class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
         if len(needle) < 1:
            return 0
         return haystack.find(needle)