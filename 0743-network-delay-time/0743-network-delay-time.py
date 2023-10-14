class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        
        for u, v, w in times:
            graph[u].append((v, w))
        
        def dijkstra(graph, start):
            distances = defaultdict(lambda: inf)
            distances[start] = 0
            visited = set()

            q = [(0, start)]

            while q:
                dis, node = heapq.heappop(q)
                if node in visited: continue

                visited.add(node)

                for neighbor, w in graph[node]:
                    distance = dis + w

                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        heapq.heappush(q, (distance, neighbor))

            if len(visited) == n:
                return distances.values()
            
            return [-1]
            
        return max(dijkstra(graph, k))