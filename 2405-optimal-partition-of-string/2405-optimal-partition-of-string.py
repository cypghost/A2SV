class Solution:
    def partitionString(self, s: str) -> int:
        lastSeen = [-1]*26
        count = 1
        substringStarting = 0

        for index in range(len(s)):
            val = ord(s[index]) - ord('a')
            
            if lastSeen[val] >= substringStarting:
                count += 1
                substringStarting = index
                
            lastSeen[val] = index

        return count