class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        number = len(boxes)
        answer = [0] * number
        
        left = 0 
        leftIndex = 0 
        right = 0
        rightIndex = 0
        
        # iterate from the left to right 
        for index in range(1, number):
            if boxes[index - 1] == '1': 
                left += 1
            
            # each step move to right, the cost increases by # of 1s on the left    
            leftIndex += left
            answer[index] = leftIndex
        
        # iterates from right to left
        for index in range(number - 2, -1, -1):
            if boxes[index + 1] == '1': 
                right += 1
            
            # each step move to left, the cost increases by # of 1s on the right 
            rightIndex += right
            answer[index] += rightIndex
        
        # return sum of the left and right loops 
        return answer
                
                