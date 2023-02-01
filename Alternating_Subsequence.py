t = int(input())
 
for x in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
 
    left = 0
    right = 0
    
    answer = 0
 
    while right < len(arr):
        
        while right < len(arr) and arr[left] * arr[right] > 0:
            if arr[left] < arr[right]:
                left = right
            
            right += 1
    
        answer += arr[left]
        left = right
    
    print(answer)
