class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def dfs(node, cur):
            cur[node] = True

            for index in range(len(bombs)):
                if not cur[index] and intersect(bombs[node], bombs[index]):
                    dfs(index, cur)
        
        def intersect(bomb1, bomb2):
            x1, y1, r1 = bomb1
            x2, y2, r2 = bomb2

            return (x1 - x2) ** 2 + (y1 - y2) ** 2 <= (r1) ** 2
        
        n = len(bombs)
        max_detonations = 0

        for index in range(n):
            visited = [False] * n
            detonations = 0

            dfs(index, visited)

            for v in visited:
                if v:
                    detonations += 1

            max_detonations = max(max_detonations, detonations)

        return max_detonations

            

            
            