class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def backtrack(start, path):
            if len(path) > 1:
                ans.append(path[:])
            
            visited = set()
            
            for index in range(start, len(nums)):
                if nums[index] not in visited:
                    if not path or nums[index] >= path[-1]:
                        visited.add(nums[index])
                        backtrack(index + 1, path + [nums[index]])
        
        backtrack(0, [])
        return ans
            
            
            
        