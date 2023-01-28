import sys
input = sys.stdin.readline
 
############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))
    
n , k = invr()
arr = inlt()
 
arr.sort()
 
if k == 0:
    print(arr[0] - 1 if arr[0] - 1 > 0 else -1)
 
elif k == n:
    print(arr[-1])
 
elif arr[k - 1] == arr[k]:
    print(-1)
 
else:
    print(arr[k] - 1 if arr[k] - 1 > 0 else -1)
