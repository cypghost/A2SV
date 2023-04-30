class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        m = len(edges)
          
        visited = set()
        graph = defaultdict(list)
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        ans = [0] * n
            
        def dfs(key, parent, cnt):
            before = cnt[labels[key]]

            for adjacent in graph[key]:
                if adjacent != parent:
                    dfs(adjacent, key, cnt)

            cnt[labels[key]] += 1
            ans[key] = cnt[labels[key]] - before

        dfs(0, 0, collections.Counter())
        return ans
        