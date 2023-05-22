class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        total = 0
        rows = len(grid)
        cols = len(grid[0])
        
        visited = set() 
        
        
		# 1. Iterate over grid and find starting position and total no. of keys.
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "@":
                    start = (i, j)
                    
                if grid[i][j] in 'abcdef':
                    total += 1
                    
        # Initiate queue using list of tuples, add starting position to queue (row, col, set(keys), no. of moves)
        queue = [(start[0], start[1], tuple(), 0)] 
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] 
        
        while queue:
            i, j, keys, moves = queue.pop(0) 
            
            # only check if that position has not already been visited whilst we have the same collection of keys.
            if (i, j, keys) not in visited: 
                visited.add((i, j, keys))  
                
                # if no of keys we have obtained is equal to total then we have found the minimum number of moves.
                if len(set(keys)) == total: 
                    return moves
                
                for x, y in directions:
                    new_keys = set(keys) 
                    
                    row, col = i + x, j + y 
                    
                    # if the row and column is in range of grid and not a wall.
                    if row >= 0 and col >= 0 and row < rows and col < cols and grid[row][col] != '#': 
                        if grid[row][col] in 'ABCDEF' and grid[row][col].lower() not in new_keys:
                            continue 
                            
                        # then we do not have the key for this lock and cannot pass
                        if grid[row][col].islower() and grid[row][col] != '.':
                            new_keys.add(grid[row][col]) 
                            queue.append((row, col, tuple(new_keys), moves+1))

                        
                        else:
                            # havent obtained a new key but is a valid move
                            queue.append((row, col, tuple(new_keys), moves+1)) 
                            
        return -1 