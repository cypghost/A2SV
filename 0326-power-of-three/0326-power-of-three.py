class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        return True if n == 1 else False if n < 1 else self.isPowerOfThree(n / 3)