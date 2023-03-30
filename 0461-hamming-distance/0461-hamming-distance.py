class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = 0
        
        for index in range(max(x, y).bit_length()):
            ans += (x & 1 << index) != (y & 1 << index)
        
        return ans
    
        # return (x ^ y).bit_count()