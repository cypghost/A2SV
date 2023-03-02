class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(" ")
        index = len(s) - 1
        
        while index >= 0:
            if s[index] == "":
                index -= 1
                
            else:
                break
            
        return len(s[index])