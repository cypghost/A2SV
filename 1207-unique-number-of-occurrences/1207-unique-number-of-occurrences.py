class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        memo = Counter(arr)
        count = 0
        
        ans = []
        
        for i in memo:
            ans.append(memo[i])
            
        if len(set(ans)) != len(ans):
            return False
        
        return True