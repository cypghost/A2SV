class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        a = money
        money -= prices[0] + prices[1]
        
        return money if money >= 0 else a