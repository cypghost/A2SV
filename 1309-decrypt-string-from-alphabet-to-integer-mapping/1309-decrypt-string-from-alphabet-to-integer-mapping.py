class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = []
        index = 0
        
        while index < len(s):
            
            if index + 2 < len(s) and s[index + 2] == '#':
                character = int(s[index : index + 2])
                ans.append(chr(character + 96))
                index += 3 
                
            else:
                ans.append(chr(int(s[index]) + 96))
                index += 1 
                
        return ''.join(ans)
    
 
#         for i in range(26,0,-1): s = s.replace(str(i)+'#'*(i>9),chr(96+i))
#         return s
