class Solution:
    def countArrangement(self, n: int) -> int:
        nums = list(range(1, n + 1))
        self.count = 0
        
        def backtrack(start):
            if start == n:
                self.count += 1
            
            for index in range(start, n):
                nums[start], nums[index] = nums[index], nums[start]
                
                if nums[start] % (start + 1) == 0 or (start + 1) % nums[start] == 0:
                    backtrack(start + 1)

                nums[start], nums[index] = nums[index], nums[start]
        
        backtrack(0)
        return self.count