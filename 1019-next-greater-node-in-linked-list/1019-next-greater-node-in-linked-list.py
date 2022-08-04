# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        result = []
        stack = []
        idx = 0
        node = head
        while node:
            while stack and node.val > stack[-1][0]:
                _, i = stack.pop()
                result[i] = node.val
                
            stack.append((node.val, idx))
            result.append(0)
            
            idx += 1
            node = node.next
            
        return result
             