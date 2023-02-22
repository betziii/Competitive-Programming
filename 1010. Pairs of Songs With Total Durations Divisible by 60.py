class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        p = 0
        dicts = collections.defaultdict(int)
        
        for i in time:
            if not i % 60:
                p += dicts[0]
            else:
                p += dicts[60 - (i % 60)]
            dicts[i % 60] += 1
        return p
