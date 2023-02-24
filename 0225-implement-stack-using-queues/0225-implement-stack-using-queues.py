class MyStack:

    def __init__(self):
        self.stack = []
        # self.up = -1
        
    def push(self, x: int) -> None:
        self.stack.append(x)
        # self.up += 1
        
    def pop(self) -> int:
        if not self.empty():
            return self.stack.pop()
            # value = self.stack[self.up]
            # self.stack.remove(self.stack[self.up])
            # self.up -= 1
            
            # return value
    

    def top(self) -> int:
        return self.stack[-1]
        # return self.stack[self.up]    
    
    def empty(self) -> bool:
        return (len(self.stack) == 0)
        # return (self.up == -1)


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()