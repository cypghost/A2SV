class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        for index in range(len(s) - 1, len(s)//2 - 1 , -1):
            temp = s[index]
            s[index] = s[-1-index]
            s[-1-index] = temp
        
        # for index in range(len(s) - 1, len(s)//2 - 1 , -1):
        #     s[index], s[-1-index] = s[-1-index], s[index]
            
          
        # return s.reverse()
        