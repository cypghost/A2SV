class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges))]
        
        def rep(x):
            if parent[x] == x:
                return x
            
            parent[x] = rep(parent[x])
            
            return parent[x]
        
        def union(x, y):
            x = rep(x)
            y = rep(y)
            
            if x != y:
                parent[x] = y
        
        def connected(x, y):
            return rep(x) == rep(y)
        
        for edge in edges:
            x, y = edge
            x -= 1
            y -= 1
            
            if connected(x, y):
                return [x + 1, y + 1]
            
            union(x, y)
        
        return []