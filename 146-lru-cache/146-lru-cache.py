class ListNode:
    def __init__(self, key, val=0, next=None, prev = None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dicts = {}
        self.left = ListNode(0,0)
        self.right = ListNode(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        

    def get(self, key: int) -> int:
        if key in self.dicts:
            self.delete(self.dicts[key])
            self.insert(self.dicts[key])
            return self.dicts[key].val
        return -1
            

    def put(self, key: int, value: int) -> None:
        if key in self.dicts:
            self.delete(self.dicts[key])
        temp = ListNode(key, value)
        self.dicts[key] = temp
        self.insert(temp)
        if self.capacity < len(self.dicts):
            lru = self.left.next
            self.delete(lru)
            del self.dicts[lru.key]
        
    def insert(self, node):
        temp = self.right.prev
        self.right.prev.next = node
        node.prev = temp
        node.next = self.right
        self.right.prev = node
        
        
    
    
    def delete(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        
        
            
    

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)