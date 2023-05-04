class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            top = heapq.heappop(stones)
            smash = abs(abs(heapq.heappop(stones)) - abs(top))
            heapq.heappush(stones, -smash)
            
        return abs(stones[0])