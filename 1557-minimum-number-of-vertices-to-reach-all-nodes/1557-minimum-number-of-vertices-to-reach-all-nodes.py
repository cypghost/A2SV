class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        arr = set(range(n))
        
        for edge in edges:
            if edge[1] in arr:
                arr.remove(edge[1])
                
        return arr
            
        