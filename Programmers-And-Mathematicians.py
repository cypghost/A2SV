t = int(input())
 
for _ in range(t):
    n , m = map(int, input().split())
    
    left = -1
    right = min(n , m)
    add = n + m
    
    while left < right - 1:
        mid = left + (right - left) // 2
        
        if mid >= add // 4:
            right = mid
        
        else:
            left = mid
        
    print(right)