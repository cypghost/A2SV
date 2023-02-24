class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips = sorted(trips, key=lambda trip:trip[2])
        
        pre_sum = []
        add = 0
        
        arr = [0] * (trips[len(trips) - 1][2] + 1)
        
        for trip in trips:        
            arr[trip[1]] += trip[0]
            arr[trip[2]] -= trip[0]
             
        for index in range(len(arr)):
            add += arr[index]
            pre_sum.append(add)
        
        if max(pre_sum) <= capacity:
            return True
        
        return False
    
        
        
             