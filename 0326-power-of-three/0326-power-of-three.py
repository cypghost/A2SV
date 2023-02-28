class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        # return True if n == 1 else False if n < 1 else self.isPowerOfThree(n / 3)
        
        
        return n > 0 and 1162261467 % n == 0