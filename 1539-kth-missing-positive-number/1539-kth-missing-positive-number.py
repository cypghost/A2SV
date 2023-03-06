class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        for index in range(1, 10001):
            if index not in arr:
                 k -= 1
            
            if k == 0:
                return index
                break
        
        return 0
        
                    