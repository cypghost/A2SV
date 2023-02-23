class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        freq_map = {}
        max_freq = 0
        ans = 0
        
        while right < len(s):
            freq_map[s[right]] = freq_map.get(s[right], 0 ) + 1
            
            max_freq = max(max_freq, freq_map[s[right]])
            
            while right - left + 1 - max_freq > k:
                freq_map[s[left]] -= 1
                left += 1
            
            ans = max(ans, right - left + 1)
            right += 1
            
        return ans
            
                
            
            
                
            