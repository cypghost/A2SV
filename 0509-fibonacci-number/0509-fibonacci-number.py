class Solution:
    def fib(self, n: int) -> int:
        return n if n == 1 or n == 0 else self.fib(n - 1) + self.fib(n - 2)