class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # APPROACH 1 : Set
        
        str_set = set()
        length = start = 0
        
        for index, char in enumerate(s):
            while char in str_set:
                str_set.remove(s[start])
                start += 1
            
            str_set.add(char)
            length = max(length, index - start + 1)
        
        return length
    
        # APPROACH 2 : Two Pointers
        
#         left = 0
#         right = 1
#         length = 0
        
#         while right <= len(s):
#             if len(set(s[left : right])) != len(s[left : right]):
#                 left += 1
                
#             length = max(length, right - left)
#             right += 1
            
#         return length

        # APPROACH 3 : Dictionary 
    
#         start = maxLength = 0
#         usedChar = {}
        
#         for i in range(len(s)):
#             if s[i] in usedChar and start <= usedChar[s[i]]:
#                 start = usedChar[s[i]] + 1
#             else:
#                 maxLength = max(maxLength, i - start + 1)

#             usedChar[s[i]] = i

#         return maxLength
