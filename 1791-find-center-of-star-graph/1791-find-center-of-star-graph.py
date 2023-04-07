class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges)
        graph = defaultdict(int)

        for index in range(n):
            row = edges[index]
    
            for idx in range(len(row)):
                graph[row[idx]] += 1
      
        val = max(graph.values())
        
        for key in graph:
            if graph[key] == val:
                return key
