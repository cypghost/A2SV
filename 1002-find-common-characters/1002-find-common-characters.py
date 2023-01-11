class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        letters = set(list(words[0]))
        answer = []
        
        for letter in letters:
            minletter = words[0].count(letter)
            
            for word in words:
                minletter = min(word.count(letter), minletter)
                
            for count in range(minletter):
                answer.append(letter)
          
        return answer
                
                
        