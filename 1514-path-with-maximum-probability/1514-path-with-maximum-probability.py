class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)

        for i in range(len(edges)):
            a, b = edges[i]
            w = succProb[i]

            graph[a].append((b, w))
            graph[b].append((a, w))

        def dijkstra(graph, start, end):
            distances = defaultdict(lambda: 0)
            distances[start] = 1
            visited = set()
            priority_queue = [(-1, start)]

            while priority_queue:
                current_distance, current_node = heappop(priority_queue)
                current_distance *= -1
                if current_node in visited:
                    continue

                visited.add(current_node)

                for neighbor, weight in graph[current_node]:
                    distance = current_distance * weight

                    if distance > distances[neighbor]:
                        distances[neighbor] = distance

                    heappush(priority_queue, (-distance, neighbor))

            return distances[end]
        
        return dijkstra(graph, start_node, end_node)