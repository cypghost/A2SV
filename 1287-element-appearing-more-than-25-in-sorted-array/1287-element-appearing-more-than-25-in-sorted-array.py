class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        apperance = ceil(n * 0.25)
        
        elements = Counter(arr)
        a = sorted(elements, reverse=True)
        
        for i in a:
            if elements[i] >= apperance:
                return i
            