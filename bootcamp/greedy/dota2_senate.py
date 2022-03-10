class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        d = deque()
        r = deque()
        
        for i in range(len(senate)):
            if senate[i] == 'R':
                r.append(i)
            else:
                d.append(i)
        # print(r, d)
        while r and d:
            val_r = r.popleft()
            val_d = d.popleft()
            if val_r < val_d:
                r.append(val_r + len(senate))
            elif val_r > val_d:
                d.append(val_d + len(senate))
        if r:
            return "Radiant"
        if d:
            return "Dire"
        