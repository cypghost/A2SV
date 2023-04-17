class Solution:
    def reverse(self, x: int) -> int:
        val = 0
        
        if str(x)[0] == '-':
            val =  int('-' + str(x)[1:][::-1])
        
        else:
            val = int(str(x)[::-1])
            
        
        if val > 2 ** 31 - 1 or val < -2 ** 31:
            return 0
        
        return val