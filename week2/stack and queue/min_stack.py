class MinStack:

    def __init__(self):
        self.s = []

    def push(self, val: int) -> None:
        self.s.append(val)
        # print(self.s)

    def pop(self) -> None:
        if len(self.s) >0:
            self.s.pop()

    def top(self) -> int:
        if len(self.s) >0:
            return self.s[-1]
        

    def getMin(self) -> int:
        if len(self.s) >0:
            # self.s.sort()
            # print(self.s)
            return min(self.s)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()