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
                
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends