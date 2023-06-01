class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        
        def fb(n):
            if n in memo:
                return memo[n]

            if n <= 1:
                return n

            if n <= 2:
                return 1

            memo[n] = fb(n - 1) + fb(n - 2) + fb(n - 3)
            
            return memo[n]

        return fb(n)