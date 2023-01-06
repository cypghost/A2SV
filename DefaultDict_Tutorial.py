# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n, m = map(int, input().split())
d = defaultdict(list)

for index in range(n):
    d[input()].append(index + 1)

for index in range(m):
    B = input()
    
    if B in d:
        print(*d[B])
    
    else:
        print(-1)
    
