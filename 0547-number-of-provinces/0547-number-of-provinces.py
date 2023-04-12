class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        count = 0
        visited = set()
        
        for index in range(len(isConnected)):
            row = isConnected[index]
            
            # if len(set(isConnected[index])) == 1:
            #     return 1
            
            for idx in range(len(row)): 
                if row[idx] == 1 and index != idx: 
                    graph[index + 1].append(idx + 1)
        
        def dfs(key):
            visited.add(key)
            
            for child in graph[key]:
                if child not in visited:
                    dfs(child)
            
        for element in range(1, len(isConnected) + 1):
            if element not in visited:
                dfs(element)
                count += 1
        
        return count
            
            
            

        
        
            
        
        