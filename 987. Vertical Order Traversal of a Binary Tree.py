# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        l_items = collections.defaultdict(list)
        q = collections.deque([(root, 0, 0)])
        
        minc = float('inf')
        maxc = float('-inf')
        
        while q:
            node, r, c = q.popleft()
            if c < minc:
                minc = c
            if c > maxc:
                maxc = c
            l_items[c].append((node.val, r))
            if node.left:
                q.append((node.left, r + 1, c - 1))
            if node.right:
                q.append((node.right, r + 1, c + 1))
        result = []
        for l in range(minc, maxc + 1):
            item = l_items[l]
            item.sort(key = lambda x: (x[1], x[0]))
            item = [val for val, _ in item]
            result.append(item)
        return result
        
