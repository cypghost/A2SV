class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0]) 
        Heap = []
        
        for row in range(m):
            for col in range(n):
                
                heappush(Heap, -matrix[row][col])
                
                if len(Heap) > k:
                    heappop(Heap)
                    
        return -heappop(Heap)