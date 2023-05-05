class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        
        for u, v in edges: 
            graph[u].append(v)
            graph[v].append(u)

        def solve(u, p):
            res = (hasApple[u], 0)

            for v in graph[u]:
                if v == p: 
                    continue

                apple, cost = solve(v, u)

                if apple: 
                    res = (True, res[1] + cost + 2)
            
            return res

        return solve(0, -1)[1]