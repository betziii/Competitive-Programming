class ListNode:
    def __init__(self, val=0, next=None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev
class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = ListNode(homepage)
        self.point = self.homepage
        
        

    def visit(self, url: str) -> None:
        self.new = ListNode(url)
        self.new.prev = self.point
        self.point.next = self.new
        self.point = self.point.next
        

    def back(self, steps: int) -> str:
        while steps:
            if self.point.prev:
                self.point = self.point.prev
                steps -= 1
            else:
                break
        return self.point.val
        

    def forward(self, steps: int) -> str:
        while steps:
            if self.point.next:
                self.point = self.point.next
                steps-=1
            else:
                break
        return self.point.val
            
    


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)