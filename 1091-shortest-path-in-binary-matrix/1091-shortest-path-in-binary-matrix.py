class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0 or grid[-1][-1] != 0: 
            return -1

        row = len(grid)
        col = len(grid[0])
        
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1), (1, -1), (-1, -1), (-1, 1), (1, 1)]
        queue = deque()
        
        dist = [[float('inf')] * (col) for _ in range(row)]

        dist[0][0] = 1 
        queue.append((0, 0, dist[0][0]))    
        
        while queue:
            currRow, currCol, currDistance = queue.popleft()

            for dr, dc in dirs:
                r = currRow + dr
                c = currCol + dc

                if r in range(row) and c in range(col) and grid[r][c] == 0:
                    if dist[r][c] > currDistance + 1: 
                        dist[r][c] = currDistance + 1 
                        queue.append((r, c, dist[r][c]))

        if dist[-1][-1] == float('inf'): 
            return -1

        return dist[-1][-1]
