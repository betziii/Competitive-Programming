# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        
        linkedlist = ListNode
        ans = linkedlist
        while head : 
            arr.append(head.val)
            head = head.next
            
        arr.sort()

        length = len(arr)
        i = 0
        for i in range(length):
            linkedlist.next=ListNode(arr[i])
            linkedlist= linkedlist.next
            
            
        
        return ans.next
