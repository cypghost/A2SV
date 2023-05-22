class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # Create Adjaceny List for Stop : [Buses that travel through that stop]
        graph = defaultdict(list)
        
        for i, stops in enumerate(routes):
            for stop in stops:
                graph[stop].append(i)
        
        # BFS Traversal 
        queue = deque()
        queue.append([source,0])
        travelled_route = set()
        
        while queue:
            stop, buses_taken = queue.popleft()
            
            if stop == target:
                return buses_taken
            
            for bus in graph[stop]:
                if bus not in travelled_route:
                    
                    for s in routes[bus]:
                        queue.append([s, buses_taken+1])
                        
                    travelled_route.add(bus)
                
        return -1