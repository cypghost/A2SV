class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        
        while low < high:  
            mid = (low + high) // 2
        
            if sum(ceil(idx / mid) for idx in piles) > h:
                low = mid + 1
                
            else:
                high = mid
        
        return high
                
            
                
                
            
            
            
            
            
            
         