# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        self.prev = prev
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.head = head
        self.left = head
        self.bool = False
        self.ls = []
        
        while self.left:
            # right = self.left.next
            self.ls.append(self.left.val)
            
            self.left = self.left.next
        #if the list is equal to the reverse of the list it is palindrome 
        if self.ls == self.ls[::-1]:
            return True
        else: 
            return False
        
        
        
            
            
            