class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        pairMap = defaultdict(int)
        prefer = {}
        
        for p1,p2 in pairs:
            pairMap[p1] = p2
            pairMap[p2] = p1
        
        for i in range(len(preferences)):
            for j in range(n-1):
                if i not in prefer:
                    prefer[i] = {}

                prefer[i][preferences[i][j]] = j
        
        res = 0

        for i in range(len(preferences)):
            for j in range(n-1):
                x = i
                y = pairMap[x]
                u = preferences[x][j]
                v = pairMap[u]

                if prefer[x][u] < prefer[x][y] and prefer[u][x] < prefer[u][v]:
                    res += 1
                    break

        return res