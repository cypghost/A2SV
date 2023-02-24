class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        pos = [0 for i in range(len(s)+1)] 
        
        for shift in shifts:
            if shift[2]: 
                pos[shift[0]] += 1  
                pos[shift[1] + 1] -= 1 
                
            else: 
                pos[shift[0]] -= 1  
                pos[shift[1] + 1] += 1 
                
        cur = 0 
        res = ""
        
        for index in range(len(s)):
            cur += pos[index]
            res += chr((cur + ord(s[index]) - 97) % 26 + 97)
            
        return res