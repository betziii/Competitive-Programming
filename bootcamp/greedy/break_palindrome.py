class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        palindrome = list(palindrome)
        if len(palindrome) == 1: return ""
        left = 0
        right = len(palindrome)
        broken = False
        
        mid = left + (right - left)//2
        for i in range(mid):
            if palindrome[i] != "a" and broken == False:
                palindrome[i] = "a"
                broken = True
                return "".join(palindrome)
                
           
        palindrome[-1] = chr(ord(palindrome[-1]) + 1)
        broken = True
        return"".join(palindrome)
                
         
        