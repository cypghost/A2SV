class Solution:
    def balancedString(self, s: str) -> int:
        s_dict = Counter(s)
        n = len(s) // 4
        
        repeat = {}
        
        for key in s_dict:
            
            if s_dict[key] > n:
                repeat[key] = s_dict[key] - n
        
        if not repeat:
            return 0
        
        left = 0
        res = len(s)
        
        for right in range(len(s)):
            
            if s[right] in repeat:
                repeat[s[right]] -= 1
            
            while max(repeat.values()) <= 0:
                res = min(res, right - left + 1)
                
                if s[left] in repeat:
                    repeat[s[left]] += 1
                    
                left += 1
                
        return res   