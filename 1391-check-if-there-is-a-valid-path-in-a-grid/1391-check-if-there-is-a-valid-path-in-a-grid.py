class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_x] = root_y
            self.rank[root_y] += 1

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        uf = UnionFind(m * n)

        directions = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }

        for row in range(m):
            for col in range(n):
                street = int(grid[row][col])

                for dr, dc in directions[street]:
                    new_row, new_col = row + dr, col + dc

                    if 0 <= new_row < m and 0 <= new_col < n:
                        next_street = int(grid[new_row][new_col])

                        for next_dr, next_dc in directions[next_street]:
                            next_row = new_row + next_dr
                            next_col = new_col + next_dc
                            
                            if next_row == row and next_col == col:
                                uf.union(row * n + col, new_row * n + new_col)

        return uf.find(0) == uf.find(m * n - 1)

