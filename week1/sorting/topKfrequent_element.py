from typing import Counter, List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter=Counter(nums)
        frequency=sorted(counter,key=lambda x:counter[x],reverse=True)
        return frequency[:k]
 
        