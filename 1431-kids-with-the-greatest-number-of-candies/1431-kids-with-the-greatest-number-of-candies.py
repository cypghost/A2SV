class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        
        for candy in candies:
            sums = candy + extraCandies
            
            print(sums, max(candies))
            
            if sums >= max(candies):
                ans.append(True)
            
            else:
                ans.append(False)
        
        return ans