class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        source = '\n'.join(source) + '\n'
        
        index = 0
        answer = ''
        
        while index < len(source):
            if index < len(source) - 1 and source[index] + source[index + 1] == '//':
                code = source.index('\n', index + 2)
                index = code
                
            elif index < len(source) - 1 and source[index] + source[index + 1] == '/*':
                code = source.index('*/', index + 2)
                index = code + 2
                
            else:
                answer += source[index]
                index += 1
                
        return [char for char in answer.split('\n') if char]  
        
        
        
        
        
        
        
        
        
        
        
        
#         num = 0
#         answer = [[] for element in range(len(source))]
        
#         while num < len(source):
#             for index in range(len(source[num])):
#                 if source[0][index] != '/':
#                     answer.append(source[0][index])
                    
#                 elif source[0][index] == '/':
#                     if source[0][index + 1] != '/':
#                         remove(source[0][index:])
                        
                        