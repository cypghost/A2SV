# Enter your code here. Read input from STDIN. Print output to STDOUT
happiness = 0
n = input().split()
arr = input().split()
A = set(input().split())
B = set(input().split())
for i in arr:
    if i in A:
        happiness += 1
    if i in B:
        happiness += -1  
print(happiness)
