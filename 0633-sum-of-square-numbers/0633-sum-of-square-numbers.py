from math import sqrt

class Solution:
    def judgeSquareSum(self, c: int) -> bool:       
        root = int(c**0.5)
        
        left = 0
        right = root
        
        while left <= right:
            
            result = left ** 2 + right ** 2
            
            if result == c:
                return True
            
            elif result > c:
                right -= 1
                
            else:
                left += 1
            
        return False 