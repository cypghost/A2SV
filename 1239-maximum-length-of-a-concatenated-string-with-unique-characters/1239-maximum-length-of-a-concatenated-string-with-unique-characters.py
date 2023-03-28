class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.res = 0
        
        def backtrack(arr, start, local):
            if len(local) != len(set(local)):
                return

            self.res = max(self.res, len(local))
            
            for index in range(start, len(arr)):
                backtrack(arr, index + 1, local + arr[index])
                
        backtrack(arr, 0, "")
        
        return self.res