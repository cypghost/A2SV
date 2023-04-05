class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n=len(words)
        
        bits = [0] * n
        lengths = [0] * n
        
        for index in range(n):             
            for char in words[index]:
                bits[index] |= 1 << (ord(char) - ord('a')) 

            lengths[index] = len(words[index])
                        
        val = 0

        for index in range(n):
            for itr in range(index + 1, n):
                if not (bits[index] & bits[itr]):
                    val = max(val, lengths[index] * lengths[itr])
        
        return val 