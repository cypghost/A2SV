class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            
            elif token == "-":
                token1 = stack.pop()
                token2 = stack.pop()
                stack.append(token2 - token1)
            
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            
            elif token == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b / a))
            
            else:
                stack.append(int(token))
                
        return stack[0]