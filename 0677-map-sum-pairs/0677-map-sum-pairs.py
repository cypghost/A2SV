class MapSum:

    def __init__(self):
        self.diction = {}

    def insert(self, key: str, val: int) -> None:
        self.diction[key] = val

    def sum(self, prefix: str) -> int:
        ans = 0
        
        for key in self.diction:
            if key.startswith(prefix):
                ans += self.diction[key]
        
        return ans

        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)