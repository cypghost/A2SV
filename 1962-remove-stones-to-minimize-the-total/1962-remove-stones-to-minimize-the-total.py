class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-pile for pile in piles]
        heapify(heap)
        for index in range(k):
            val = heappop(heap)
            ans = ceil(-val / 2)
            
            heappush(heap, -ans)
        
        return -(sum(heap))