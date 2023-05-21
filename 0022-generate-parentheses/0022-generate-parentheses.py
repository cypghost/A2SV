class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def isValid(p_string):
            left_count = 0
            
            for p in p_string:
                if p == '(':
                    left_count += 1
                    
                else:
                    left_count -= 1

                if left_count < 0:
                    return False
                
            return left_count == 0
        
        answer = []
        queue = collections.deque([""])
        
        while queue:
            cur_string = queue.popleft()

            if len(cur_string) == 2 * n:
                if isValid(cur_string):
                    answer.append(cur_string)
                    
                continue
                
            queue.append(cur_string + ")")
            queue.append(cur_string + "(")
            
        return answer