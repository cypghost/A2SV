class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        distance=[[0 for idx in range(n)] for index in range(m)]
        visited=[[0 for idx in range(n)] for index in range(m)]

        q = deque()

        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0:
                    visited[row][col] = 1
                    q.append([row, col, 0])
        
        while len(q) > 0:
            row, col, dist = q.popleft()

            for r, c in [(row, col - 1), (row, col + 1), (row - 1, col), (row + 1, col)]:
                if 0 <= r < m and 0 <= c < n and visited[r][c] == 0:
                    visited[r][c] = 1
                    distance[r][c] = dist + 1
                    q.append([r, c, distance[r][c]])

        return distance
        