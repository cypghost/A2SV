class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def neighbours(end):
            res = []
            
            for index in range(4):
                updated = str((int(end[index]) + 1) % 10)
                res.append(end[:index] + updated + end[index + 1:])
                
                updated = str((int(end[index]) - 1) % 10)
                res.append(end[:index] + updated + end[index + 1:])
                
            return res
            
        visited = set(deadends)

        if '0000' in visited:
            return -1

        q = deque([('0000', 0)])

        while q:
            end, moves = q.popleft()

            if end == target:
                return moves

            for neighbour in neighbours(end):
                if neighbour not in visited:
                    q.append((neighbour, moves + 1))
                    visited.add(neighbour)
        return -1