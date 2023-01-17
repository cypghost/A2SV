#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        selectionSort(arr, i)
    
    def selectionSort(self, arr,n):
        #code here
        for index in range(len(arr)):
            minindex = index
            
            for element in range(index, len(arr)):
                if arr[element] < arr[minindex]:
                    minindex = element
                
            arr[index], arr[minindex] = arr[minindex], arr[index]
