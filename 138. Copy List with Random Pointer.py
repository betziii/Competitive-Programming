# """
# # Definition for a Node.
# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random
# """

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        ptr = head
        while ptr:
            new_node = Node(ptr.val)
            new_node.next = ptr.next
            ptr.next = new_node
            ptr = new_node.next
        ptr = head
        while ptr:
            if ptr.random:
                ptr.next.random = ptr.random.next
            ptr = ptr.next.next

        odd = head
        even = new_head = head.next
        while even and even.next:
            odd.next = even.next
            odd = even.next
            even.next = odd.next
            even = odd.next
        odd.next = even.next

        return new_head
