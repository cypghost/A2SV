class Solution:
    def reverseBits(self, n: int) -> int:
        m = bin(n)
        m = m[2:][::-1]
        
        for _ in range(32 - n.bit_length()):
            m += '0'
        
        
        return int(m, 2)
        
        