class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
	
	# TIME LIMIT EXCEEDED        
#         number = 0
#         add = 0
        
#         while number < len(spaces):
            
#             s = s[:spaces[number] + add] + " " +s[spaces[number] + add:]
#             number += 1
#             add += 1
        
#         return s

        answer = []
        number = 0
        
	# stores a word to the list separately from the string
        for index in spaces:
            word = s[number:index]
            answer.append(word)
            number = index
            
        # left out string characters are added 
        answer.append(s[spaces[len(spaces) - 1]:])
        
        return " ".join(answer)
        
        
			
