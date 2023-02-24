class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        
        left = 0
        
        while left <  len(s):
            if s[left] != '*':
                stack.append(s[left])
            
            else:
                stack.pop()
            
            left += 1
                
        return ''.join(stack)