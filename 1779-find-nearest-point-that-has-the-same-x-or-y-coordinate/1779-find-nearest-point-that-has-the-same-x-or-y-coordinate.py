class Solution(object):
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        
        maximum = float('inf')
        answer = -1
        
        for index in range(len(points)):
            if points[index][0] == x or points[index][1] == y:
                distance = abs(x - points[index][0]) + abs(y - points[index][1])
                
                if distance < maximum:
                    answer = index
                    maximum = distance
                    
        return answer
                    
                