class MyCircularQueue:

    def __init__(self, k: int):
        self.cap = k
        self.q = [0] * k
        self.ct = 0
        self.head = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q[(self.head + self.ct) % self.cap] = value
        self.ct += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.cap
        self.ct -= 1
        return True

    def Front(self) -> int:
        if not self.ct:
            return -1
        return self.q[self.head]

    def Rear(self) -> int:
        if not self.ct:
            return -1
        return self.q[(self.head + self.ct - 1) % self.cap]

    def isEmpty(self) -> bool:
        return self.ct == 0

    def isFull(self) -> bool:
        return self.ct == self.cap
# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
