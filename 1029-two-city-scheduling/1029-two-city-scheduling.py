class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int: 
        n, difference = len(costs), {}
        sumA, sumB = 0, 0
        
        for index in range(n):
            difference[index] = costs[index][0] - costs[index][1]
        
        difference = sorted(difference.items(), key=lambda x:x[1])
        
        for index in range(n):
            if index < n // 2:
                sumA += costs[difference[index][0]][0]
            
            else:
                sumB += costs[difference[index][0]][1]
        
        return sumA + sumB