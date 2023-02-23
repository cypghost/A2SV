class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = 0
        s1_dict = Counter(s1)
        s2_dict = defaultdict(int)
        
        if len(s1) > len(s2):
            return False
        
        for right in range(len(s1)):
            s2_dict[s2[right]] += 1
            
        if s1_dict == s2_dict:
            return True
        
        while left < len(s2) - len(s1):
            s2_dict[s2[left]] -= 1
            
            if s2_dict[s2[left]] == 0:
                del s2_dict[s2[left]]
            
            left += 1
            
            if right < len(s2) - 1:
                right += 1
                s2_dict[s2[right]] += 1
            
            if s2_dict == s1_dict:
                return True
        
        return False
            
            
            