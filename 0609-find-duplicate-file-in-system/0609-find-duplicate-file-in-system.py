class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        file = defaultdict(lambda :[])
        
        for index in range(len(paths)):
            string = paths[index]
            word = string.split(" ")                
            
            for char in range(1, len(word)):
                brac = word[char].index("(")
                file[word[char][brac:]].append(word[0] + "/" + word[char][:brac])
                    
        return [file[index] for index in file if len(file[index]) > 1] 
         
#         answer = [[] for element in range(2)]
        
#         for elements in range(len(paths)):
#             path = paths[elements]
#             for char in range(len(path)):
#                 if path[char] == '(':
#                     if path[char + 1] == 'a':
#                         answer[element].append(path[0:char])
                
#             for char in range(len(path)):
#                     if path[char] == '(':
#                         if path[char + 1] =='e':
#                             answer[element - 1].append(path[0:char])
    
#         return answer
