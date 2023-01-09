class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        dic = defaultdict(lambda :[])
        
        for index in range(len(paths)):
            string = paths[index]
            word = string.split(" ")                
            
            for char in range(1, len(word)):
                sp = word[char].index("(")
                dic[word[char][sp:]].append(word[0] + "/" + word[char][:sp])
                    
        return [dic[index] for index in dic if len(dic[index]) > 1]


        
        
        
        
        
        
        
        
        
        
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