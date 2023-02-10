class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ls = nums1 + nums2
        ls.sort()
        l = 0
        r=len(ls) - 1
        m=(l + r) // 2
        if(len(ls) % 2 == 0):
            return((ls[m] + ls[m + 1])/ 2)
        else:
            return ls[m]
