from pip import Optional

from linked_list.add_two_numbers import ListNode


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        val = head
        count = 0
        while val != None:
            count += 1
            val = val.next
        
        for i in range(count//2):
            head = head.next
        
        return head