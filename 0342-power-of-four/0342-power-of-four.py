class Solution:
    def isPowerOfFour(self, n: int) -> bool:
 
        if n == 1:
            return True
    
        elif n < 1:
             return False
        
        # n = n / 4
        
        return self.isPowerOfFour(n / 4)
        