from sortedcontainers import SortedList

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        tree = SortedList()
        counter = Counter()
        cost = 0
        
        for idx, val in enumerate(instructions):
            tree.add((val, idx))
            place = tree.index((val, idx))
            
            cost += min(place - counter[val], idx - place)
            counter[val] += 1
            
        return cost % 1000000007