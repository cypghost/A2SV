class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        biggest = 0
        second_biggest = 0
        
        for num in nums:
            if num > biggest:
                second_biggest = biggest
                biggest = num
            
            else:
                second_biggest = max(second_biggest, num)
        
        second_biggest -= 1
        biggest -= 1
    
        return biggest * second_biggest
        
        