# Enter your code here. Read input from STDIN. Print output to STDOUT

A = int(input())
setA = set(map(int, input().split()))
B = int(input())
setB = set(map(int, input().split()))

print(len(setA.difference(setB)))
