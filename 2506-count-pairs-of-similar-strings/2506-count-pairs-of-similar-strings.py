class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        count = 0
        
        for index, char in enumerate(words):
            
            for letter in words[index + 1:]:
                
                if set(char) == set(letter):
                    count += 1
                
        return count