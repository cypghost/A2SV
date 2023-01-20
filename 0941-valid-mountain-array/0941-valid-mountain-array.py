class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        '''
        
        The first and last elements of the array need to be the lowest compared to those in the middle
        
        
        
        '''
        # 1. check if arr length < 3
        if len(arr) < 3:
            return False
        
        # 2. check if there exists equal  element next to eachother
        for index in range(len(arr)-1):
            if arr[index] == arr[index + 1]:
                return False
            
        # 3. find the peak of the mountain array and its index
        peak = 0
        value = 0
        
        for index in range(len(arr)):
            if arr[index] > peak:
                peak = arr[index]
                value = index
                
        if value == 0:
            return False
    
        if value == len(arr) - 1:
            return False
        
        for index in range(value - 1):
            if arr[index] > arr[index + 1]:
                return False
            
        for index in range(value, len(arr) - 1):
            if arr[index] < arr[index + 1]:
                return False       
        
        return True
        