class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        b = []
        sub = []
        maxl = 0
        
        for i in range(len(s)):
            j = i
            
            while j < len(s):
                x = s[j]
                
                if x in b:
                    if len(b)>maxl:
                        maxl = len(b)
                        
                    sub.append(''.join(b))
                    b.clear()
                    break
                
                else:
                    b.append(s[j])
                    j+=1
                    
        sub.append(''.join(b))
        
        if len(b)> maxl:
            maxl = len(b)
            
        return maxl
    
        # APPROACH 1
        
#         left = 0
#         right = 1
#         length = 0
        
#         while right <= len(s):
#             if len(set(s[left : right])) != len(s[left : right]):
#                 left += 1
                
#             length = max(length, right - left)
#             right += 1
            
#         return length

        # APPROACH 2 
    
#         start = maxLength = 0
#         usedChar = {}
        
#         for i in range(len(s)):
#             if s[i] in usedChar and start <= usedChar[s[i]]:
#                 start = usedChar[s[i]] + 1
#             else:
#                 maxLength = max(maxLength, i - start + 1)

#             usedChar[s[i]] = i

#         return maxLength