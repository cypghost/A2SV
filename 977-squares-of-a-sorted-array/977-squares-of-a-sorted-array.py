import numpy as np 

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:      
        nums1 = np.square(nums)
        nums1.sort()
        
        return nums1
        