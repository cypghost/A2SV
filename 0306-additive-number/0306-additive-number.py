class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        ans = []
        
        def backtrack(start, nums):
            nonlocal ans
            
            if start == len(nums) and len(ans) >= 3:
                return True 
            
            for index in range(start, len(nums)):
                if nums[start] == "0" and index != start:
                    break
                    
                val = int(nums[start : index + 1])
                
                if len(ans) >= 2  and ans[-2] + ans[-1] < val:
                    break
                
                if len(ans) <= 1 or ans[-2] + ans[-1] == val:
                    ans.append(val)
                    
                    if backtrack(index + 1,  nums):
                        return True
                    
                    ans.pop()
            
            return False
    
        backtrack(0, num)
        
        return len(ans) > 0