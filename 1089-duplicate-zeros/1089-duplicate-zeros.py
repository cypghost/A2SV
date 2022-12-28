class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        num = arr.count(0)
        
        if num == 0:
            return arr
        
        number = 0
        
        while number < len(arr):
            if arr[number] == 0:
                arr.pop()
                arr.insert(number,0)
                number += 1
            number += 1
                 
    
                
                