class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        lookup = defaultdict(dict)
        maxi = 0

        for i, _num in enumerate(nums):
            # check against existing sequences
            if len(lookup[_num]) > 0:
                for _increment, _length in lookup.pop(_num).items():
                    _target = _num + _increment
                    _length += 1
                    if _length > maxi: maxi = _length
                    lookup[_target][_increment] = max(lookup[_target].get(_increment, 0), _length)
            
            # new 2-term sequences
            for j in range(i):
                _increment = _num - nums[j]
                _target = _num + _increment
                if maxi < 2: maxi = 2
                lookup[_target][_increment] = max(lookup[_target].get(_increment, 0), 2)  
        
        return maxi
