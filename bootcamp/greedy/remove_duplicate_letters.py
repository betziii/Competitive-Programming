from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        stack = []
        for i in s:
            if i in stack:
                count[i]-= 1
                continue
            while stack and i < stack[-1] and count[stack[-1]] > 1:
                count[stack[-1]] -= 1
                stack.pop()
            stack.append(i)
        return "".join(stack)