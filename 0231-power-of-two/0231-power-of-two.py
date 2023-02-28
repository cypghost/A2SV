class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # return 1 if n == 1 else 0 if n < 1 else self.isPowerOfTwo(n / 2)
        
        return n > 0 and 2**31 % n == 0