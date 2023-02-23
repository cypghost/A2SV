class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        right = 0
        maxlen = 0
        count = defaultdict(int)
        
        while right < len(fruits):
            if (len(count) == 2 and fruits[right] in count) or len(count) < 2:
                maxlen = max(maxlen, right - left + 1)
                
                count[fruits[right]] += 1
                
                right += 1
            
            else:
                count[fruits[left]] -= 1
                
                if count[fruits[left]] == 0:
                    del count[fruits[left]]
                    
                left += 1
            
        return maxlen