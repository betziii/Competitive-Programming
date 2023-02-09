class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(start):
            if len(octs) == 4 and start == len(s):
                ips.append('.'.join(octs))
                return
            
            for size in range(1, 4):
                oc = s[start:start + size]
                if len(oc) > 1 and (oc[0] == '0' or int(oc) > 255):
                    continue
                if len(octs) < 4:
                    octs.append(oc)
                    backtrack(start + size)
                    octs.pop()
        octs = []
        ips = []
        backtrack(0)
        return ips
