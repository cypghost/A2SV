# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())

for index in range(T):
    num = int(input())
    cubes = list(map(int,input().split()))
    answer = "Yes"
    
    # To see if its possible to stack the cubes
    while len(cubes) > 1:
        if cubes[0] >= cubes[-1]:
            largenum = cubes[0]
            cubes.pop(0)  
               
        else:
            largenum = cubes[-1]
            cubes.pop(-1)  
            
        if largenum < cubes[0] or largenum < cubes[-1]:
            answer = "No"
            break
          
    print(answer)
