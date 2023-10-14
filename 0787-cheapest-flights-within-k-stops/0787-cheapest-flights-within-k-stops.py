from heapq import *

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(dict)

        for u, v, w in flights:
            graph[u][v] = w
        
        visited = {}
        heap = []
        heappush(heap, (0, 0, src))
        
        while heap:
            cost, k_count, city = heappop(heap)
            visited[city] = k_count
            
            if city == dst:
                return cost
            
            if k_count > k:
                continue
            
            for next_city, next_cost in graph[city].items():
                if next_city in visited and visited[next_city] <= k_count:
                    continue
                    
                heappush(heap, (cost + next_cost, k_count + 1, next_city))
        
        return -1