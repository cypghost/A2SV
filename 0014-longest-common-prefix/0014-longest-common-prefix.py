class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        size = len(strs)
        
        if size == 0:
            return " "
        
        elif size == 1:
            return strs[0]
        
        strs.sort()
        end = min(len(strs[0]), len(strs[size - 1]))
        index = 0
        
        while index < end and strs[0][index] == strs[size - 1][index]:
                  index += 1
                
        pre = strs[0][0:index]
        
        return pre
                  
