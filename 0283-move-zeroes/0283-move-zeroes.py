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
            