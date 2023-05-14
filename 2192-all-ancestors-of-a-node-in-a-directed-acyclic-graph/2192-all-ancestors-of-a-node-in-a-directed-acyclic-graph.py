class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        queue = deque()
        bloodlines = [[] for i in range(n)]
        
        in_degree = [0] * n
        traversal = [[] for i in range(n)]
        
        for (a,b) in edges:
            in_degree[b] += 1
            traversal[a].append(b)
        
        hashset = set()
        for index, ancestors in enumerate(in_degree):
            if ancestors == 0:
                queue.append(index)
            
        while queue:
            parent = queue.popleft()
            
            for child in traversal[parent]:
                in_degree[child] -= 1
                bloodlines[child].append(parent)
                bloodlines[child] = list(set(bloodlines[child] + bloodlines[parent]))
                
                
                if in_degree[child] == 0:
                    queue.append(child)
                
        for bloodline in bloodlines:
            bloodline.sort()
            
        return bloodlines