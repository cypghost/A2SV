class OrderedStream:

    def __init__(self, n: int):
        self.ans = [""] * n
        self.ptr = 0
        
    def insert(self, idKey: int, value: str) -> List[str]:
        self.ans[idKey - 1] = value
        a = self.ptr
        
        while self.ptr < len(self.ans) and self.ans[self.ptr] != "":
            self.ptr += 1
        
        return self.ans[a:self.ptr]
        
        
# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)