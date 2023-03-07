class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left = 1
        right = max(time) * totalTrips

        def timeEnough(given_time):
            actual_trips = 0
            
            for t in time:
                actual_trips += given_time // t
                
            return actual_trips >= totalTrips
        
        
        while left < right:
            
            mid = (left + right) // 2
            
            if timeEnough(mid):
                right = mid
                
            else:
                left = mid + 1
                
        return left