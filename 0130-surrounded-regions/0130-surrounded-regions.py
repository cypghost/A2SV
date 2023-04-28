class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        visited = set()

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(row, col):
            
            if not 0 <= row < m or not 0 <= col < n:
                return False
            
            if (row, col) in visited or board[row][col] == 'X':
                return True

            surrounded = True

            changed.add((row, col))

            visited.add((row, col))

            for r, c in dirs:
                surrounded &= dfs(row + r, col + c)
            
            return surrounded

        def changedfs(changed):
            for r, c in changed:
                board[r][c] = 'X' 
                print(board[r][c])
            
        for row in range(m):
            for col in range(n):
                
                if board[row][col] == 'O' and (row, col) not in visited:
                    changed = set()
                    
                    if dfs(row, col):
                        changedfs(changed)
            
        return board










