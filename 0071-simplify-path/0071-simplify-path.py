class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        n = len(path)
        s = path.split("/")
        
        for char in s:
            if char == "" or char == ".":
                continue
                
            elif char == "..":
                if stack:
                    stack.pop()
                
            else:
                stack.append(char)  
        
        return "/"+"/".join(stack)
                
            
                
                
                
        
                  