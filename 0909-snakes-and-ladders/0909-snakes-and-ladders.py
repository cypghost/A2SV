class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # BFS
        self.n = len(board)
        goal = self.n * self.n
        
        queue = [(1, 0)]
        # using a set to remember the visited cell
        visited = set()
        
        while queue:
            cur, step = queue.pop(0)

            if cur == goal:
                return step
            
            for move in range(1, 7):
                cell = cur + move

                if cell > goal:
                    break
                    
                r, c = self.row2col(cell)

                if (r, c) not in visited:
                    visited.add((r, c))

                    if board[r][c] != -1:
                        cell = board[r][c]

                    queue.append((cell, step + 1))
        
        return -1
                        
                        
    def row2col(self, n):        
        row = (n - 1) // self.n
        
        row = self.n - row - 1
        col = (n - 1) % self.n

        if (self.n - row) % 2 == 0:
            col = self.n - col - 1

        return row, col