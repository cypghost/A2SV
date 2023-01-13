from collections import defaultdict

t = int(input())

for index in range(t):
    n, m = map(int, input().split())
    elements = [list(map(int, input().split())) for j in range(n)]
    
    rightsum = defaultdict(int)
    leftsum = defaultdict(int)

    for row in range(n):
        for col in range(m):   
            rightsum[row + col] += elements[row][col]
            leftsum[row - col] += elements[row][col]
        
    answer = 0
    for row in range(n):
        for col in range(m):
            temp = rightsum[row + col] + leftsum[row - col] - elements[row][col] 
            answer = max(answer, temp)

    print(answer)
