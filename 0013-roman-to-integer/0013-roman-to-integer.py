class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        number = 0
        
        for index in range(len(s) - 1):
            if roman[s[index]] < roman[s[(index + 1)]]:
                number -= roman[s[index]]
            
            else:
                number += roman[s[index]]
                
        return number + roman[s[-1]]

        