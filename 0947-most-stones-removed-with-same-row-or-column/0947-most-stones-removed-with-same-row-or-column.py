class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def find(x):
            if x == parent[x]:
                return x
            
            else:
                parent[x] = find(parent[x])
                return parent[x]
            
        def union(u, v):
            root_u, root_v = find(u), find(v)
            
            if root_u == root_v:
                return 
            
            if size[root_v] > size[root_u]:
                parent[root_u] = root_v
                size[root_v] += size[root_u]
                
            else:
                parent[root_v] = root_u
                size[root_u] += size[root_v]
        
        n = len(stones)
        r = c = 0
        
        for a, b in stones:
            r = max(r, a)
            c = max(c, b)
            
        parent = [i for i in range(r + c + 2)]
        
        size = [1 for i in range(r + c + 2)]
        d = {} 
        
        for a, b in stones:
            union(a, b + r + 1)
            d[a] = 1
            d[b + r + 1] = 1
            
        c = 0
    
        for key in d:
            if find(key) == key:
                c += 1
                
        return n - c