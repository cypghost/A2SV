class DataStream:

    def __init__(self, value: int, k: int):
        self.stream = []
        self.value = value
        self.k = k
        
    def consec(self, num: int) -> bool:
        if num != self.value:
            self.stream = []
            return False

        self.stream.append(num)

        if len(self.stream) > self.k:
            del self.stream[0]
    
        return (self.stream and self.stream[0] == self.value and len(self.stream) == self.k)


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)