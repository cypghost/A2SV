class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        subsequences = []
        
        for num in nums:
            while subsequences and subsequences[0][0] + 1 < num:
                sub = heapq.heappop(subsequences)
                
                if sub[1] < 3:
                    return False
            
            if not subsequences or subsequences[0][0] == num:
                heapq.heappush(subsequences, [num, 1]) # end, len
                
            else:
                # Pop and push to maintain order
                sub = heapq.heappop(subsequences)
                
                sub[0] += 1
                sub[1] += 1
                
                heapq.heappush(subsequences, sub)
                
        while subsequences:
            sub = heapq.heappop(subsequences)
            
            if sub[1] < 3:
                return False
            
        return True