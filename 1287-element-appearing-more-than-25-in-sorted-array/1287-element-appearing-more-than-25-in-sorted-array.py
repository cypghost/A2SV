class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        counts = defaultdict(int)
        target = len(arr) / 4
        
        for num in arr:
            counts[num] += 1
            
            if counts[num] > target:
                return num

        return -1
            