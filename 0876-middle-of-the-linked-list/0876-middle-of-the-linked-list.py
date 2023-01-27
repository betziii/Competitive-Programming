# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left=head           #1   2   3  4
        right= head         #1   3   5  none

        while right and right.next:
            left=left.next
            right=right.next.next
        return left