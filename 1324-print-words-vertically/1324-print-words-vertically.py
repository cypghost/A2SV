class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        s = s.split(" ")
        answer = []
        
        maxlength = max(len(word) for word in s)
        
        for index in range(maxlength):
            verword = ""
            
            for word in s:
                if len(word) > index:
                    verword += word[index]
                    
                else:
                    verword += " "
                    
            answer.append(verword)
        
        output = []
        
        for verword in answer:
            output.append(''.join(verword).rstrip())
            
        return output
        
        
        