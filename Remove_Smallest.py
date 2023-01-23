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
                        
t = inp()

for value in range(t):
    n = inp()
    arr = inlt()
    
    arr.sort()
    case = True
    
    for index in range(len(arr) - 1):
        if not arr[index + 1] - arr[index] <= 1:
            case = False
        
    if case:
        print("YES")
        
    else:
        print("NO")
             
# WRONG ON TEST CASE 2

# t = inp()

# for index in range(t):
#     n = inp()
#     arr = inlt()
    
#     arr.sort()
#     for index in range(len(arr) - 1):
#         if not arr[index + 1] - arr[index] <= 1: 
#             print("NO")
        
#         elif arr[index + 1] - arr[index] <= 1 and index == len(arr) - 2:
#             print("YES")
