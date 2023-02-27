class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def cmp(x, y):
            for i in x:
                if y[i] < x[i]:
                    return False
            return True
            
            
        left = 0
        s_dict = Counter(t)
        t_dict = Counter(t)
        res = s + s + s
        
        if len(t) > len(s):
            return ""
        
        if s == t:
            return t
        
        for index in s_dict:
            s_dict[index] = 0
            
        for right in range(len(s)):
            if s[right] in s_dict:
                s_dict[s[right]] += 1
            
            while cmp(t_dict, s_dict):
                if len(res) > right - left + 1:
                    res = s[left : right + 1]
                    
                s_dict[s[left]] -= 1 
                left += 1
            
        return res if res != s+s+s else ""
        
            
                
            
            
            
            
        