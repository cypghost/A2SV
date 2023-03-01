class Solution:
    def decodeString(self, s: str) -> str:
        def decode(s, index):
            ans = ""
            digit = 0
            
            while index < len(s):
                
                if s[index].isdigit():
                    digit = digit * 10 + int(s[index])
                    
                elif s[index] == '[':
                    Str, index = decode(s, index + 1)
                    ans += digit * Str
                    digit = 0
                    
                elif s[index] == ']':
                    
                    return ans, index
                else:
                    ans += s[index]
                    
                index += 1
            
            return ans

        return decode(s, 0)
                        
        
        
        # stack=[]
            
        # for char in s:
            
        #     if char == "]":
                
        #         Str = ""
                
        #         while stack[0] != "[":
        #             Str = stack.pop(0) + Str
                
        #         stack.pop(0)
                
        #         digit = ""
                
        #         while stack and stack[0].isdigit():
        #             digit = stack.pop(0) + digit
                
        #         stack.insert(0, int(digit) * Str)
                
        #     else:
        #         stack.insert(0, char)
            
        # stack.reverse()
        
        # ans = ""
        
        # for index in stack:
        #     if not index.isdigit():
        #         ans += index
            
        # return ans
