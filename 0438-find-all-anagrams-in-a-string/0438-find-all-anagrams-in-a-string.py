class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) >len(s):
            return []
        
        s_dict = defaultdict(int)
        p_dict = Counter(p)
        
        ans = []
        
        left = 0
        right = 0
        
        for right in range(len(p)):
            s_dict[s[right]] += 1
            
        if s_dict == p_dict:
                ans.append(left)
                        
        while left < len(s) - len(p):
            s_dict[s[left]] -= 1
            
            if s_dict[s[left]] == 0:
                del s_dict[s[left]]
            
            left += 1
            
            if right < len(s) - 1:
                right += 1
                s_dict[s[right]] += 1
            
            if s_dict == p_dict:
                ans.append(left)
            
        return ans
            
            
            
        
        