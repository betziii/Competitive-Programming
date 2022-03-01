# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        sums = 0
        return self.recur(root,sums,targetSum)
    def recur(self, current, sums, target):
        if not current:
            return False
        if not current.left and not current.right:
            return sums + current.val == target
        
        if self.recur(current.left, sums + current.val, target):
            return True
        return self.recur(current.right, sums + current.val, target)