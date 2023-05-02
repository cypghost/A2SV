class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = 1
        
        for num in nums:
            product *= num
            
        return -1 if product < 0 else 1 if product > 0 else 0