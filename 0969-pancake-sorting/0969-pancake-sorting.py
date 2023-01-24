class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        size = len(arr)
        ans = []
        
        while size > 1:
            
            large = arr.index(size)
                
            if large == size - 1:
                size -= 1
                continue

            elif large != 0:
                arr[:large + 1] = reversed(arr[:large + 1])
                ans.append(large + 1) 
            
            arr[:size] = reversed(arr[:size])
            ans.append(size)
                
            size -= 1 
            
        return ans  
