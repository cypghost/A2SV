class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        ans = [[0] * k for _ in range(k)]
		
        def topological(condition):
            graph = defaultdict(list)
            incoming = [0] * k

            for a, b in condition:
                graph[a].append(b)
                incoming[b - 1] += 1
            
            queue = deque()

            for i, val in enumerate(incoming):
                if val == 0:
                    queue.append(i + 1)
                    
            order = []
            
            while queue:
                curr = queue.popleft()
                order.append(curr)
                
                for child in graph[curr]:
                    incoming[child - 1] -= 1
                    if incoming[child - 1] == 0:
                        queue.append(child)
                        
            return order
                        
        row_order = topological(rowConditions)
        col_order = topological(colConditions)
        
        #cycle detection
        if len(row_order) < k or len(col_order) < k:
            return []
        
        for row, val in enumerate(row_order):
            col = col_order.index(val)
            ans[row][col] = val
            
        return ans