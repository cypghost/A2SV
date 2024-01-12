class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        a = 0
        
        for i in range(n):
            if s[i] in  {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}:
                if i < n // 2:
                    a += 1

                else:
                    a -= 1
            
        if a == 0:
            return True
        
        return False