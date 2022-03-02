class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        return self.summ(root)[1]
        
    def summ(self, cur):
        if not cur:
            return 0, 0
        if not cur.left and not cur.right:
            return cur.val, 0
        
        leftsum, lefttilt = self.summ(cur.left)
        rightsum, righttilt = self.summ(cur.right)
        
        tilt = abs(leftsum - rightsum)
        
        cur_tilt = lefttilt+ righttilt + tilt
        
        cur_sum = leftsum + rightsum + cur.val
        return cur_sum, cur_tilt
        
        