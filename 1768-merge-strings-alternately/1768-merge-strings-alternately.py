class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Initialiaztion
        pointer = 0
        merged = ""
        num = min(len(word1), len(word2))
        
        # append elements
        while pointer < num:
            merged += word1[pointer]
            merged += word2[pointer]
            pointer += 1
          
        merged += word1[pointer:]
        merged += word2[pointer:]
        return merged
        