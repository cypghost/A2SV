class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
#         Solution 3: 65% runtime 95% space 
#         for index in range(len(s) - 1, len(s)//2 - 1 , -1):
#             temp = s[index]
#             s[index] = s[-1-index]
#             s[-1-index] = temp

#         Solution 2: 99% runtime 
#         for index in range(len(s) - 1, len(s)//2 - 1 , -1):
#             s[index], s[-1-index] = s[-1-index], s[index]
            
#         Solution 1: 96% runtime  
          return s.reverse()
        
