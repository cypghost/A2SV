class LockingTree:
    def __init__(self, parent: List[int]):
        self.parent = parent
        self.locked = [[False, 0]]
        self.child = defaultdict(list)
        
        for index in range(1,len(parent)):
            self.child[parent[index]].append(index)
            self.locked.append([False, 0])

    def lock(self, num: int, user: int) -> bool:
        if not self.locked[num][0]:
            self.locked[num] = [True, user]
            
            return True
        
        return False

    def unlock(self, num: int, user: int) -> bool:
        if self.locked[num][0] and self.locked[num][1] == user:
            self.locked[num] = [False, 0]
            
            return True
        
        return False
    
    def check_parent(self, start):
        if self.locked[start][0]:
            return False
        
        if self.parent[start] != -1:
            return self.check_parent(self.parent[start])
        
        return True
            
    def upgrade(self, num: int, user: int) -> bool:
        count = 0
        
        def unlock_children(start, visited):
            nonlocal count
            
            if start in visited:
                return
            
            visited.add(start)

            for child in self.child[start]:
                if self.locked[child][0] == True:
                    count += 1
                    self.locked[child][0] = False
                    
                unlock_children(child, visited)
                
        visited = set()
        
        if not self.locked[num][0]:
            if self.check_parent(num):
                unlock_children(num, visited)
                
                if count > 0:
                    self.locked[num] = [True, user]
                    
                    return True
        
        return False
        



# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)










