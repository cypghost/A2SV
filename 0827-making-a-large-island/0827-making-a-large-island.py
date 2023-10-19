class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        area = 0
        
        def dfs(r,c,idx):
            grid[r][c] = idx
            nonlocal area
            area += 1

            for dr, dc in [[-1,0],[1,0],[0,-1],[0,1]]:
                nr, nc = r + dr, c + dc

                if nr >= 0 and nr < rows and nc < rows and nc >= 0 and grid[nr][nc] == 1:
                    dfs(nr,nc,idx)
        
        label = 2
        hashmap = {}

        for r in range(rows):
            for c in range(rows):
                if grid[r][c] == 1:
                    area = 0
                    dfs(r,c,label)
                    hashmap[label] = area
                    label += 1
        
        if len(hashmap) == 0: 
            return 1

        _max = max(hashmap.values())

        for r in range(rows):
            for c in range(rows):
                if grid[r][c] == 0:
                    res = 1
                    visit = set()

                    for dr, dc in [[-1,0],[1,0],[0,-1],[0,1]]:
                        nr, nc = r + dr, c + dc

                        if nr >= 0 and nr < rows and nc < rows and nc >= 0 and grid[nr][nc] != 0 and grid[nr][nc] not in visit:
                            res += hashmap[grid[nr][nc]]
                            visit.add(grid[nr][nc])

                    _max = max(_max, res)
        
        return _max