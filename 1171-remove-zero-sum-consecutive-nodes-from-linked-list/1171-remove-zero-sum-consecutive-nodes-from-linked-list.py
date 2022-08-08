# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sums, dict1 = 0, {}
        dict1[0] = temp = ListNode(0)
        cur = temp.next = head

        while cur:
            sums += cur.val
            dict1[sums] = cur
            cur = cur.next

        head, sums = temp, 0

        while head:
            sums += head.val
            head.next = dict1[sums].next
            head = head.next

        return temp.next
            
        