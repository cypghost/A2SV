class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        self.size = 0
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if self.size == 0 or self.minstack[-1] >= val:
            self.minstack.append(val)
            
        self.size += 1
        
    def pop(self) -> None:
        x = self.stack.pop()
        
        if x == self.minstack[-1]:
            self.minstack.pop()
            
        self.size -= 1   
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()