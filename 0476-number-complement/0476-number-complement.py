class Solution:
    def findComplement(self, num: int) -> int:    
        for index in range(num.bit_length()):
            num ^= 1 << index
            
        return num