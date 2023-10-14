class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:  
        dictionary = defaultdict(int)
        sumA, sumB = 0, 0

        for index in range(len(costs)):
            dictionary[index] = costs[index][0] - costs[index][1]

        dictionary = sorted(dictionary.items(), key=lambda x:x[1])
        
        for index in range(len(dictionary)):
            if index < len(dictionary) // 2:
                sumA += costs[dictionary[index][0]][0]

            if index >= len(dictionary) // 2:
                sumB += costs[dictionary[index][0]][1]

        return sumA + sumB