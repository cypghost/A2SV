class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        memo = defaultdict(list)
        
        for i in range(len(nums) - 1, -1, -1):
            for j in range(len(nums[i])):
                memo[i + j].append(nums[i][j])
        
        ans = []
        curr = 0
        
        while curr in memo:
            ans.extend(memo[curr])
            curr += 1
        
        return ans
                
                
        