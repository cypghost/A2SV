class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        length = 0
        stack = []
        
        for elem in pushed:
            stack.append(elem)
            
            while stack and length < len(popped) and stack[-1] == popped[length]:
                stack.pop()
                length += 1

        return length == len(popped)