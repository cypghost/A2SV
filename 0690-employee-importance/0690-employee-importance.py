"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = defaultdict(list)
        sums = 0
        
        for employee in employees:
            graph[employee.id].append(employee.importance)
            graph[employee.id].append(employee.subordinates)
            
        def dfs(graph, id):
            nonlocal sums
            
            ans = graph[id][1]
            sums += graph[id][0]
            
            if len(ans) == 0:
                return 
            
            for index in range(len(ans)):
                 dfs(graph, ans[index])
                
        dfs(graph, id)
        return sums
                
                    
                    