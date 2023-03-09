class Solution:
    def splitString(self, s: str) -> bool:
        curr = []

        def backtrack(idx):
            if idx >= len(s):
                return len(curr) >= 2
            
            for index in range(idx, len(s)):
                val = int(s[idx: index + 1])

                if len(curr) == 0 or val == curr[-1] - 1:
                    curr.append(val)
                    print(val, curr, s[index])
                    
                    if backtrack(index + 1):
                        return True
                    
                    curr.pop()
                
            return False
        
        return backtrack(0)