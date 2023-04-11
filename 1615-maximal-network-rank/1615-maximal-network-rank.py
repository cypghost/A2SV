class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for index in range(len(roads)):
            graph[roads[index][0]].append(roads[index][1])
            graph[roads[index][1]].append(roads[index][0])
         
        res = 0
        
        for index in range(n):
            for idx in range(index + 1, n):
                if idx in graph[index]:
                    res = max(res, len(graph[index]) + len(graph[idx]) - 1)
                    
                else:
                    res = max(res, len(graph[index]) + len(graph[idx]))
                    
        return res
    
