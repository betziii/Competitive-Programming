class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        count = collections.Counter(nums)
        cand = {x: [y for y in count if int(
            math.sqrt(x + y)) ** 2 == x + y] for x in count}
        self.result = 0

        def dfs(x, cter):
            count[x] -= 1
            if cter == 0:
                self.result += 1
            [dfs(y, cter - 1) for y in cand[x] if count[y] > 0]
            count[x] += 1

        for x in count:
            dfs(x, len(nums) - 1)

        return self.result
