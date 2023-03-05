class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
#         ans = max(arr)
        
#         left = 0
#         right = len(arr) - 1
        
#         while left <= right:
            
#             mid = (left + right) // 2
            
#             if arr[mid] == ans:
#                 return mid
        
        return arr.index(max(arr))
                