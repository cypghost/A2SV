class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
#         n, m = len(word1), len(word2)
#         a, b = "", ""
        
#         for i in range(n):
#             a += word1[i]
            
#         for i in range(m):
#             b += word2[i]
            
#         return a == b

        return "".join(word1) == "".join(word2)