# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sums = 0

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        gp = False
        p = False
        self.dfs(root, p, gp)
        return self.sums
    
    def dfs(self, root, p, gp):
        if not root:
            return
        if gp:
            self.sums += root.val
        self.dfs(root.left, root.val % 2 == 0, p)
        self.dfs(root.right, root.val % 2 == 0, p)
