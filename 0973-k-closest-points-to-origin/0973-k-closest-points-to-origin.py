class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        # distances = []
        # for point in points:
        #     distance = (point[0] ** 2 + point[1] ** 2 ) ** 0.5
        #     distances.append([point, distance])
        
        points.sort(key = lambda point: point[0] ** 2 + point[1] ** 2 )
        
#         nearest = []
        
#         for index in range(k):
#             nearest.append(distances[index][0])

        return points[:k]
       
                
                