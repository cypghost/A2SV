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
    
n = inp()
arr = inlt()
 
foundOdd = foundEven = False
 
for num in arr:
    if num % 2 == 0:
        foundEven = True
    
    else:
        foundOdd = True
    
if foundEven and foundOdd:
    arr.sort()
 
print(*arr)
