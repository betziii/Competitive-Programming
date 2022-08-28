class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = deque(s)
        for i in range(len(s)):
            a = d.popleft()
            if a not in d:
                return s.index(a)
            else:
                d.append(a)
        return -1