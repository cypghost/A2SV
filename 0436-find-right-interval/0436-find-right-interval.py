class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        coll = sorted([ [start, end, index] for index, [start, end] in enumerate(intervals)])
        
        starts = [start for start, _ , _ in coll]
        
        res = [-1] * len(starts)
        
        for start, end, index in coll:
            
            val = bisect_left(starts, end)
            
            if val < len(starts):
                res[index] = coll[val][2]
        
        return res