class Solution:
    def countOrders(self, n: int) -> int:
        if n == 1:
            return 1
        
        b = n * 2
        a = (b * (b - 1)) // 2
        
        return a * self.countOrders(n - 1) % (10**9 + 7)
        
    