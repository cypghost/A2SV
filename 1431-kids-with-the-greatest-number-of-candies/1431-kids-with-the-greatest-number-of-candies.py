class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        
        maxCandies = max(candies)
        
        for candy in candies:
            ans.append(candy + extraCandies >= maxCandies)
        
        return ans