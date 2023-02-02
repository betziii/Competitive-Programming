class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        res = []
        d = []
        l = []
        for i in logs:
            if i.split()[1].isdigit():
                d.append(i)
            else:
                l.append(i)
        l = sorted(l, key = lambda x: (x.split(' ',1)[1], x.split(' ',1)[0]))
        res += l + d
        return res
