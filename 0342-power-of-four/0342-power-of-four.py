class Solution:
    def isPowerOfFour(self, n: int) -> bool:
 
        # if n == 1:
#             return True
    
#         elif n < 1:
#              return False
    
        return True if n == 1 else False if n < 1 else self.isPowerOfFour(n / 4)
    
        # n /= 4
        
        # return self.isPowerOfFour(n)
        