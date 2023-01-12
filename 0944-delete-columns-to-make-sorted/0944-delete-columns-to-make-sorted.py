class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        count = 0
        
        for char in range(len(strs[0])):
            
            for index in range(len(strs) - 1):
                if ord(strs[index][char]) > ord(strs[index + 1][char]):
                    count += 1
                    break
        
        return count


    