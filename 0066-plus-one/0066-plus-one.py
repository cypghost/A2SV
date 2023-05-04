class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        count = 0
        multiply = 1
        
        for index in range(1, n + 1):        
            count += digits[n - index] * multiply
            multiply *= 10
        
        count += 1
        
        digits = [int(index) for index in str(count)]

        return digits