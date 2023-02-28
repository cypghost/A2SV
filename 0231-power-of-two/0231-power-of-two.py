class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return True if n == 1 else False if n < 1 else self.isPowerOfTwo(n / 2)