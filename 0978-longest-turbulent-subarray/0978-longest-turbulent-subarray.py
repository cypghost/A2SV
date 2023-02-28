class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        def cmp(before, after):
            if before > after:
                return -1
            
            elif before < after:
                return 1
            
            else:
                return 0
            
        left = 0
        ans = 1
        
        for index in range(1, len(arr)):
            val = cmp(arr[index - 1], arr[index])
            
            if val == 0:
                left = index
            
            elif index == len(arr) - 1 or val * cmp(arr[index], arr[index + 1]) != -1:
                ans = max(ans, index - left + 1)
                left = index
            
        return ans