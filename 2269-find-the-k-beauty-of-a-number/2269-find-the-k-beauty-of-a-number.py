class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        left = 0 
        ans = -float("inf")
        number = str(num)
        count = 0
        
        while left < len(number):
            if left + k <= len(number):
                part = number[left : left + k]
                
                if int(part) != 0 and num % int(part) == 0:
                    count += 1
                
                left += 1
                
            else: 
                break 
        
        return count