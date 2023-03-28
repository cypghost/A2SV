class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        path = []
        result = []
        
    
        def backtrack(s, path, result):
            if not s and len(path) == 4:
                s = '.'.join(path[::-1])
                result.append(s)
                return
            
            elif len(path) == 4:
                return 
            
            else:
                for index in range(1, min(3, len(s)) + 1):
                    if int(s[:index]) >= 0 and int(s[:index]) <= 255:
                        if index > 1 and s[0] == '0': 
                            continue
                            
                        else: 
                            backtrack(s[index:], [s[:index]] + path, result)
                return
            
        backtrack(s, path, result)
        
        return result