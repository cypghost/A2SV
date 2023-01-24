n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr3 = []

left = 0
left1 = 0

while left < n and left1 < m:
    if arr1[left] < arr2[left1]:
        arr3.append(arr1[left])
        left += 1
        
    else:
        arr3.append(arr2[left1])
        left1 += 1

while left1 != m:
    arr3.append(arr2[left1])
    left1 += 1
    
while left != n:
    arr3.append(arr1[left])
    left += 1

print(*arr3)
