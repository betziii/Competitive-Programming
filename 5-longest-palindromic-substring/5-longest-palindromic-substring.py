class Solution:
    def getPlindrome(self, s, l, r, n):
        while l >= 0 and r < n and s[l] == s[r]:
            if (r - l + 1) > self.resLen:
                self.res = s[l:r+1]
                self.resLen = r - l + 1

            l -= 1
            r += 1
                
                
    def longestPalindrome(self, s: str) -> str:
        self.res = ''
        self.resLen = 0
        n = len(s)
        for i in range(n):
            # For Odd lenght palindrome
            l, r = i, i
            self.getPlindrome(s, l, r, n)
            
            # For even length palindrome
            l, r = i, i+1
            self.getPlindrome(s, l, r, n)
            
        return self.res

        