class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def sub(word):
            index = -1

            for char in word:
                index = s.find(char, index + 1)

                if index == -1:
                    return False
                
            return True
        
        ans = 0

        for word in words:
           if sub(word):
               ans += 1
        
        return ans