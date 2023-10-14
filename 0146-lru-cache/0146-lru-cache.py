class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.used = []
        
    
    def get(self, key: int) -> int:
        if key in self.cache:
            self.put(key, self.cache[key])
            return self.cache[key]
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.used.append(self.used.pop(self.used.index(key)))
        else:
            if len(self.used) == self.capacity:
                del self.cache[self.used.pop(0)]
            self.used.append(key)
        self.cache[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)