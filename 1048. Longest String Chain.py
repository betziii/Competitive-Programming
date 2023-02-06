class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        wrds = set(words)
        m = {}
        
        def helper(word):
            if word not in wrds:
                return 0
            if word in m:
                return m[word]
            else:
                n = len(word)
                maxi = 0
                for i in range(n):
                    maxi = max(maxi, helper(word[:i] + word[i + 1:]) + 1)
                    m[word] = maxi
            return maxi
        for w in words:
            helper(w)
        return max(m.values())
