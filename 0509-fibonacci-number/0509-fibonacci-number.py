class Solution:
    def fib(self, n: int) -> int:
        return n if n < 2 else self.fib(n - 1) + self.fib(n - 2)