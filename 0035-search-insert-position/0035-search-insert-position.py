class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # O(log n) time complexity
        
        found = False
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            
            mid = (left + right) // 2
            
            if nums[mid] == target:
                found = True
                break
                
            if nums[mid] < target:
                left = mid + 1
            
            elif nums[mid] > target:
                right = mid - 1
                
        if found == False:
            return left
            
        else:
            return mid
            
        # O(n) time complexity
        
#         left = 0
#         found = False
        
#         while left < len(nums):
#             if nums[left] == target:
#                 found = True
#                 break
                
#             else:
#                 left += 1
                
#         if found == True:
#             return left
        
#         else:
#             left = 0
            
#             while left < len(nums):
#                 if target - nums[left] > 1:
#                     left += 1
                
#                 elif target - nums[left] == 1:
#                     found = True
#                     break
            
#             if found == True:
#                 return left + 1
                
            
                
        