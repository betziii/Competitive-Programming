# Definition for singly-linked list.
from pip import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
             
        str1 = ''
        str2 = ''
        while(l1!=None or l2!=None):
            if l1 != None and l2 == None:
                str1 += str(l1.val)
                l1 = l1.next
                
            elif l1 == None and l2 != None:
                str2 += str(l2.val)
                l2 = l2.next
            else:
                str1 += str(l1.val)
                str2 += str(l2.val)
                l1 = l1.next
                l2 = l2.next
        str1 = str1[::-1]
        str2 = str2[::-1]
        res = int(str1) + int(str2)
        res = str(res)
        t = ListNode(int(res[0]))
        for i in range(1, len(res)):
            temp = t
            t = ListNode(int(res[i]))
            t.next = temp
        
        return t
        
#     def string_to_ll(self,t,head):
#         head = self.add(t[0])
#         curr = head
#         for i in range(len(t) - 1):
#             curr.next = self.add(t[i + 1])
#             curr = curr.next

#         return head
#     def add(self,data):
#         newnode = ListNode()
#         newnode.data = data
#         newnode.next = None
#         return newnode       
                