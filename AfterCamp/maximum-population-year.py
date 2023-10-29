class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        population = [0] * 101
        start = 1950
        
        for l in logs:
            population[l[0] - start] += 1
            population[l[1] - start] -= 1
            
        maxi = 0
        s = 0
        ans = 1950
        
        for index, value in enumerate(population):
            s += value
            
            if s > maxi:
                maxi = s
                ans = 1950 + index
    
        return ans
                