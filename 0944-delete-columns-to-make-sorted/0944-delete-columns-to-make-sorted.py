class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        count = 0
        # Problem 1
#         pointer = 1
#         index = 0
        
#         while index < len(strs[0]) and pointer <= len(strs) - 1:
#             print(strs[pointer][index], strs[pointer - 1][index])
#             if strs[pointer][index] < strs[pointer - 1][index]:
#                     count += 1
#                     pointer += 1
#             index += 1
        
        # Problem 2 
#         pointer = 0
#         index = 0
        
#         while index < len(strs[0]) and pointer < len(strs) - 1:
#             if strs[pointer][index] > strs[pointer + 1][index]:
#                     count += 1
#                     pointer += 1
#             index += 1

        for char in range(len(strs[0])):
            for index in range(len(strs) - 1):
                if ord(strs[index][char]) > ord(strs[index + 1][char]):
                    count += 1
                    break
        
        return count




















#         for char in range(len(strs[0])):
#             for index in range(len(strs)):
#                 if ord(strs[index][char]) < ord(strs[index - 1][char]):
#                     count += 1
#                     break
                

    