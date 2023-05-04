class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        count = 0
        s = 1
        for index in range(1, len(digits) + 1):        
            count = count + digits[len(digits) - index] * s
            s *= 10
        
        count = count + 1 
        
        digits = [int(index) for index in str(count)]

        return digits