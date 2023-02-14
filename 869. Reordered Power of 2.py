class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def helper(n1):
            return sorted(list(n1))
        n1=str(n)
        s1=helper(n1)
        for i in range(0,32):
            a=str(2**i)
            if helper(a)==s1:
                if len(a)==len(n1):
                    return True
        return False
