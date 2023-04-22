class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        
        def dfs(index, path):
            if index == len(graph) - 1:
                ans.append(path)
                
            for idx in graph[index]:
                dfs(idx, path + [idx])
           
        dfs(0, [0])
        return ans
        
        