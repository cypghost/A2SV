class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        moves = {0:(1, 3), 1:(0, 2, 4), 2:(1, 5), 3:(0, 4), 4:(1, 3, 5), 5:(2, 4)}
        
        state = "".join(str(c) for c in board[0] + board[1])
        start = state.index('0')
        
        visited = set()
        
        queue = collections.deque([(start, state, 0)])
        
        while queue:
            cur, state, steps = queue.popleft()
            
            if state == '123450':
                return steps
            
            elif state in visited:
                continue
                
            else:
                visited.add(state)
                
                for nxt in moves[cur]:
                    tmp = list(state)
                    
                    tmp[cur], tmp[nxt] = tmp[nxt], tmp[cur]
                    tmp = ''.join(tmp)
                    
                    queue.append((nxt, tmp, steps + 1))
                    
        return -1
    