class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
       
        count = Counter()
    
        totalCost = 0

        def dfs(node,par,end):
            nonlocal count
            nonlocal totalCost
            
            if node == end:
                return True
            
            for nei in graph[node]:
                if nei != par:
                    if dfs(nei, node, end):
                        count[nei] += 1
                        totalCost += price[nei]
                        
                        return True
                    
            return False

       
        for start,end in trips:
            count[start] += 1
            totalCost += price[start]
            dfs(start,None,end)
        
      
        @cache
        def dp(node, par, canReduce):
            if canReduce:
                res = (price[node] // 2) * count[node]
                
            else:
                res = 0
                
            red = 0
            for nei in graph[node]:
                if nei != par:
               
                    if canReduce:
                        cur = dp(nei, node, False)

                    else:
                        cur = max(dp(nei, node, False), dp(nei, node, True))
                        
                    red += cur
                    
            return res + red
        
        reduce = 0
        for i in range(n):
            reduce = max(reduce, dp(i, None, True), dp(i, None, False) )
        
    
        return totalCost - reduce