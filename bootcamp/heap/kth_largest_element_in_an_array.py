import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        a = heapq.nlargest(k, nums)
        return a[len(a) - 1]