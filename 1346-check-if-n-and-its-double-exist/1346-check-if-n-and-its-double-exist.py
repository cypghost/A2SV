class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        temp = arr.count(2)
            
        for i in range(len(arr) - 1):
            
            for j in range(i+1,len(arr)):
                
                if arr[j] == arr[i] * 2 or arr[i] == arr[j] * 2:
                    return True
        
        return False
                
            
                
               