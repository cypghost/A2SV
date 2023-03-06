class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(weights, mid):
            count = 0
            add = 0
            
            for weight in weights:
                if add + weight > mid:
                    count += 1
                    add = 0
                    
                add += weight
                
            count += 1
            
            return count
                
        left = max(weights)
        right = sum(weights)
        
        while left < right:
            
            mid = (left + right) // 2
            
            if check(weights, mid) <= days:
                right = mid
            
            else:
                left = mid + 1
        
        return left