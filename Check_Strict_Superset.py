# Enter your code here. Read input from STDIN. Print output to STDOUT
setA = set(map(int, input().split()))
N = int(input())
answer = "True"

for index in range(N):
    setB = set(map(int, input().split()))
    
    # Checks if B is not superset of A or if length of B is greater or equal to A
    if not setA.issuperset(setB) or len(setB) >= len(setA):
        answer = "False"
        
print(answer)
