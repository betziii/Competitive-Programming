class Solution:
    def validPalindrome(self, s: str) -> bool:
        def helper(lf, rh):
            while lf < rh:
                if s[lf] == s[rh]:
                    lf += 1
                    rh -= 1
                else:
                    return False
            return True
        
        n = len(s)-1
        l,r = 0, len(s)-1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return helper(l,r-1) or helper(l+1,r) 
        return True
