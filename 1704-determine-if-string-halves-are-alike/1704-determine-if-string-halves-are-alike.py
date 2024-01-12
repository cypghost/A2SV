class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        a, b = 0, 0
        
        for i in range(n):
            if s[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                if i < n // 2:
                    a += 1

                else:
                    b += 1
            
        if a == b:
            return True
        
        return False