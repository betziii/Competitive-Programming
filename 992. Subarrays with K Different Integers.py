class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def getKcount(k):
#            dict = {}
            distincts = 0

            i,j = 0,0
            n = len(nums)
            count = 0

            while j < n:
                dict[nums[j]] = 1 if not nums[j] in dict else dict[nums[j]] + 1
                if dict[nums[j]] == 1: distincts += 1
                if distincts > k:
                    while distincts > k:
                        dict[nums[i]] -= 1
                        # If the integer removed results in its count becoming 0, that means one distinct integer has been removed from the window
                        if dict[nums[i]] == 0: distincts -= 1
                        i += 1
                count += j - i + 1
                j += 1

            return count
        return getKcount(k) - getKcount(k - 1)
        
