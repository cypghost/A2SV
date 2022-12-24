class Solution:
    def interpret(self, command: str) -> str:
        
        # Space to Keep our strings
        answer = ""
        
        # To find strings and "()" to replace with o
        for i in range(len(command)):
            if command[i] != "(" and command[i] != ")":
                answer += command[i]
                    
            elif  command[i] == "(" and command[i+1] == ")":
                answer += "o"
        return answer          
        
            
            
