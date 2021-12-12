class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        lst = []
        lst1 = sorted(nums)
        l = len(nums)

        for i in range(l):
            if lst1[i] == target:
                lst.append(i)
        return lst