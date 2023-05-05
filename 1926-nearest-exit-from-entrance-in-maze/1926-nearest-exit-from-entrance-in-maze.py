class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        row = len(maze)
        col = len(maze[0])
        
        visited = set()
        queue = deque()

        queue.append((tuple(entrance), 0))
        
        while queue:
            elem = queue.popleft()
            
            pos = elem[0]
            step = elem[1]
            
            if (pos[0] < 0 or pos[0] > row - 1 or pos[1] < 0 or pos[1] > col - 1 or pos in visited or maze[pos[0]][pos[1]] == '+'):
                continue
            
            if (pos[0] == 0 or pos[0] == row - 1 or pos[1] == 0 or pos[1] == col - 1):
                if step != 0:
                    return step

            visited.add(pos) 
            
            queue.append(((pos[0]+1, pos[1]), step+1))
            queue.append(((pos[0], pos[1]+1), step+1))
            queue.append(((pos[0]-1, pos[1]), step+1))
            queue.append(((pos[0], pos[1]-1), step+1))
            
        return -1