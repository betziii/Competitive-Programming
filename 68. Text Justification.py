class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ls = []
        result = []
        n = 0
        for word in words:
            while len(word) + n + len(ls) > maxWidth:
                space = (len(ls) - 1) or 1
                q, r = divmod(maxWidth - n, space)
                for i in range(space):
                    ls[i] += " " * q + (" " if i < r else "")
                result.append("".join(ls))
                n, ls = 0, []
                
            ls.append(word)
            n += len(word)
        return result + [" ".join(ls).ljust(maxWidth)] if ls else []
