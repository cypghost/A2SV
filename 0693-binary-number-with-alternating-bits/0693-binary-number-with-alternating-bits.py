class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        val = list(bin(n))
        
        for index in range(len(val) - 1):
            if val[index] == val[index + 1]:
                return False
        
        return True