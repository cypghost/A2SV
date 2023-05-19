class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        parent = [i for i in range(n + 1)]
        
        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]
        
        def connected(u, v):
            return find(1) == find(u) == find(v)

        def union(u, v):
            root_u, root_v = find(u), find(v)

            if root_u != root_v:
                parent[root_u] = root_v
        
        mini = float("inf")

        for road in roads:
            u, v, dist = road
            union(u, v)

        root1 = find(1)
        for road in roads:
            u, v, dist = road

            if connected(u, v):
                mini = min(mini, dist)
        
        return mini