class DSU:
    def __init__(self, n):
        self.n = n
        self.par = [-1 for _ in range(n)]
        self.rank = [1 for _ in range(n)]
    
    def findPar(self, z):
        if self.par[z] == -1:
            return z
        self.par[z] = self.findPar(self.par[z])
        return self.par[z]
    
    def union(self, a, b):
        if self.rank[a] < self.rank[b]:
            a, b = b, a
        self.par[b] = a
        self.rank[a] += int(self.rank[a] == self.rank[b])


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        dsu = DSU(n)
        for a, b in pairs:
            u = dsu.findPar(a)
            v = dsu.findPar(b)
            if u != v:
                dsu.union(u, v)
        
        groups = {}
        for i in range(n):
            z = dsu.findPar(i)
            if z not in groups:
                groups[z] = []
            groups[z].append(i)
        
        ans = ["a" for _ in range(n)]
        for group in groups.values():
            temp = [s[i] for i in group]
            temp.sort()
            for j in range(len(group)):
                ans[group[j]] = temp[j]
        
        return "".join(ans)