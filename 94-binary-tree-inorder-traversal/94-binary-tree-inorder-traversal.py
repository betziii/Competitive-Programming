# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        current = root
        while True:
            
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                node = stack.pop()
                if node.val != None:
                    result.append(node.val)
                current = node.right
            else:
                return result
