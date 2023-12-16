class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dics_s, dics_t = Counter(s), Counter(t)
        
        for i in s:
            if i not in dics_t or dics_s[i] != dics_t[i]:
                return False
        
        for i in t:
            if i not in dics_s or dics_s[i] != dics_t[i]:
                    return False    
        
        return True
        