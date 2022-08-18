class FreqStack:

    def __init__(self):
        self.stack = defaultdict(list)
        self.frequency = Counter()
        self.maxf = 0

    def push(self, val: int) -> None:
        v = self.frequency[val] + 1
        self.frequency[val] = v
        if v > self.maxf:
            self.maxf = v
        self.stack[v].append(val)

    def pop(self) -> int:
        v = self.stack[self.maxf].pop()
        self.frequency[v] -= 1
        if not self.stack[self.maxf]:
            self.maxf -= 1
        
        return v


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()