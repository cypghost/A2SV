class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        color = [0] * len(graph)
        order = []
        
        def dfs(node):
            if color[node] == 2:
                return False
        
            if color[node] == 1:
                return True
            
            color[node] = 1
        
            for neighbor in graph[node]:
                cycle_found = dfs(neighbor)
                
                if cycle_found:
                    return True
            
            color[node] = 2
            order.append(node)
            return False
        
        for index in range(len(graph)):
            dfs(index)
                
        order.sort()
        return order
        
        
                