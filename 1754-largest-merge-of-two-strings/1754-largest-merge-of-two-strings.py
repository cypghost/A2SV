class Solution(object):
    def largestMerge(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merge = ""
        
        word1ptr = 0
        word2ptr = 0
        
        word1start = 0
        word2start = 0
        
        while word1ptr < len(word1) and word2ptr < len(word2):
            if word1[word1ptr] == word2[word2ptr]:
                if word1[word1start:] > word2[word2start:]:
                    merge += word1[word1start]
                    word1start += 1
                    word1ptr += 1
                    
                else:
                    merge += word2[word2start]
                    word2start += 1
                    word2ptr += 1
                    
            elif word1[word1ptr] > word2[word2ptr]:
                merge += word1[word1start]  
                
                word1start += 1
                word1ptr = word1start
                
                word2ptr = word2start
            
            elif word1[word1ptr] < word2[word2ptr]:
                merge += word2[word2start]
                
                word2start += 1
                word2ptr = word2start
                
                word1ptr = word1start
                
            
        
        return max(merge + word2[word2start:] + word1[word1start:] , merge + word1[word1start:] + word2[word2start:])
                   