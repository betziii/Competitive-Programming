class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(map(int, str(num)))
        dicts = {val:i for i, val in enumerate(num)}
        
        for idx, value in enumerate(num):
            for s in range(9, value, -1):
                if s in dicts and dicts[s] > idx:
                    num[idx], num[dicts[s]] = num[dicts[s]], num[idx]
                    return int("".join(map(str, num)))
        return int("".join(map(str, num)))
