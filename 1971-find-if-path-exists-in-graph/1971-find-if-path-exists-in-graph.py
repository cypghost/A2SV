class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        m = len(edges)
        graph = defaultdict(list)
        visited = set()
        
        def dfs(source):
            if source == destination:
                return True
            
            visited.add(source)
            
            for index in graph[source]:
                if index not in visited:
                    if dfs(index):
                        return True
            
            return False
            
        for edge in edges:  
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        
        return dfs(source)
            