class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digtoletter = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        result = []
        def dfs(i, cur):
            if len(cur) == len(digits):
                result.append(cur)
                return
            for w in digtoletter[digits[i]]:
                dfs(i+1, cur + w)
        
        if digits:
            dfs(0,"")
        
        return result
        