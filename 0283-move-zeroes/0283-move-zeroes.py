from collections import deque

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = nums.count(0)
        
        for i in range(temp):
            nums.remove(0)
            nums.append(0)
            
        return nums
        
    
    
    
    
    
    
    
        q = deque(nums)
        
        for i in range(len(nums)):
            if nums[i]== 0:
                q.append(nums[i])
            else:
                q.appendleft(nums[i])
                
        return q
            