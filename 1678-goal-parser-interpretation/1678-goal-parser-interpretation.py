class Solution:
    def interpret(self, command: str) -> str:
        
        # Space to Keep our strings
        answer = ""
        
        # Check if empty or not and to find strings and "()" to replace with o
        if command == "":
            return 0
        
        else:
            for i in range(len(command)):
                if command[i] != "(" and command[i] != ")":
                    answer += command[i]
                    
                elif  command[i] == "(" and command[i+1] == ")":
                    answer += "o"
        return answer          
        
            
            