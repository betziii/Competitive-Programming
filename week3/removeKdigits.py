class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in num:
            while k and stack and stack[-1]>i:
                stack.pop()
                k-=1
            if not stack and i=='0': continue
            stack.append(i)
        return "0" if not stack or k>=len(stack) else "".join(stack[:len(stack)-k])